import os
import sys
from configparser import ConfigParser
import shutil
from mutant_dictionary import all_mutants
from mutant_dictionary import all_mutant_keys
import getfilename

class GenerateMutants():

    if not os.path.exists('./config.ini'): #Config parser - From Drew's and Luke's Code
        print("Error: Config File does not exist")
        with open('config.ini', 'w', encoding="utf-8") as f:
            f.write('testing')
            sys.exit()
    else:
        file = 'config.ini'
        config = ConfigParser()
        config.read(file)
        mutants = config.options('Mutants')
        filename = "../CMakeLists.txt"
        mutant_list = []
        active_mutants = []

        if os.path.exists('../mutants'):
            os.system("rm -r ../mutants/")

        for x in mutants: #Pareses config for mutants that are marked active
            if config.get('Mutants', x) == '1':
                mutant_list.append(x) #Creates list of active mutants from config file

        for x in all_mutant_keys:
            if x.lower() in mutant_list:
                active_mutants.append(all_mutants[x])

        if not os.path.exists('../mutants'):
            os.mkdir('../mutants')

        for i in active_mutants:  #Creates folders for all active mutants
            build_dir = '../mutants/' + i.get_name()
            if not(os.path.exists(build_dir)):
                os.mkdir(build_dir) #Creates folder
                os.mkdir(build_dir + "/src/")
                os.mkdir(build_dir + "/test/")

            with open(build_dir + "/CMakeLists.txt", "w+") as f: #Writes CMakeLists file for mutant
                f.write("add_subdirectory(src)\n")
                f.write("enable_testing()\n")
                f.write("add_subdirectory(test)\n")

            with open(build_dir + "/src/CMakeLists.txt", "w+") as f:
                f.write("add_library(example_" + i.get_name() + ")\n")
                f.write("target_sources(example_" + i.get_name() + "\n")
                f.write("  PRIVATE\n")
                for srcfile in getfilename.getFilenamesFromCMakeLists("../src/CMakeLists.txt"):
                    f.write("    " + srcfile.replace(".cpp", "_" + i.get_name() + ".cpp\n"))
                f.write("  PUBLIC\n")
                for srcfile in getfilename.getHeaderFilenamesFromCMakeLists("../src/CMakeLists.txt"):
                    f.write("    " + srcfile.replace(".h", "_" + i.get_name() + ".h\n"))
                f.write("  )\n")
                f.write("\n")
                f.write("target_include_directories(example_" + i.get_name() + "\n")
                f.write("  PUBLIC\n")
                f.write("    ${CMAKE_CURRENT_LIST_DIR}\n")
                f.write("  )")
                f.write("\n")                
                f.write("# we use this to get code coverage\n")
                f.write("# flags are only valid with the GNU compiler and on Linux\n")
                f.write("if(CMAKE_CXX_COMPILER_ID MATCHES GNU AND CMAKE_HOST_SYSTEM_NAME STREQUAL \"Linux\")\n")
                f.write("  target_compile_options(example_" + i.get_name() + "\n")
                f.write("    PUBLIC\n")
                f.write("      \"--coverage\"\n")
                f.write("    )\n")
                f.write("  target_link_options(example_" + i.get_name() + "\n")
                f.write("    INTERFACE\n")
                f.write("      \"--coverage\"\n")
                f.write("    )\n")
                f.write("endif()\n")

            with open(build_dir + "/test/CMakeLists.txt", "w+") as f:
                f.write("include(FetchContent)\n")
                f.write("FetchContent_Declare(gtest\n")
                f.write("  QUIET\n")
                f.write("  URL https://github.com/google/googletest/archive/release-1.10.0.tar.gz\n")
                f.write(")\n")
                f.write("# configure build of googletest\n")
                f.write("set(gtest_force_shared_crt ON CACHE BOOL \"\" FORCE)\n")
                f.write("set(BUILD_GMOCK OFF CACHE BOOL \"\" FORCE)\n")
                f.write("FetchContent_MakeAvailable(gtest)\n")
                f.write("\n")
                f.write("add_executable(\n")
                f.write("    unit_tests_" + i.get_name() + "\n")
                f.write("    example_add_" + i.get_name() + ".cpp\n")
                f.write("    example_subtract_" + i.get_name() + ".cpp\n")
                f.write("    )\n")
                f.write("\n")
                f.write("target_link_libraries(unit_tests_" + i.get_name() + "\n")
                f.write("  PRIVATE\n")
                f.write("  example_" + i.get_name() + "\n")
                f.write("    gtest_main\n")
                f.write("  )\n")
                f.write("\n")
                f.write("# automatic discovery of unit tests\n")
                f.write("include(GoogleTest)\n")
                f.write("gtest_discover_tests(unit_tests_" + i.get_name() + "\n")
                f.write("  PROPERTIES\n")
                f.write("    LABELS \"unit\"\n")
                f.write("  DISCOVERY_TIMEOUT  # how long to wait (in seconds) before crashing\n")
                f.write("    240\n")
                f.write("  )\n")

            with open('../mutants/CMakeLists.txt', "a+") as f:
                f.write("add_subdirectory(" + i.get_name() + ")\n")

            mutation_targets = getfilename.getFilenamesFromCMakeLists("../src/CMakeLists.txt")
            mutation_headers = getfilename.getHeaderFilenamesFromCMakeLists("../src/CMakeLists.txt")
            test_targets = getfilename.getFilenamesFromCMakeLists("../test/CMakeLists.txt")

            with open("../src/" + mutation_targets[0], "r") as input:
                with open(build_dir + "/src/" + mutation_targets[0].replace(".cpp", "_" + i.get_name() + ".cpp"), "w+") as output:
                    for line in input:
                        mutated_line = i.mutate(line)
                        final_line = mutated_line.replace(mutation_headers[0], mutation_headers[0].replace(".h", "_" + i.get_name() + ".h"))
                        output.write(final_line)

            with open("../src/" + mutation_headers[0], "r") as input:
                    with open(build_dir + "/src/" + mutation_headers[0].replace(".h", "_" + i.get_name() + ".h"), "w+") as output:
                        for line in input:
                            output.write(line)

            for test in test_targets:
                with open("../test/" + test, "r") as input:
                    with open(build_dir + "/test/" + test.replace(".cpp", "_" + i.get_name() + ".cpp"), "w+") as output:
                        for line in input:
                            modified_line = line.replace(mutation_targets[0].replace(".cpp", ""), mutation_targets[0].replace(".cpp", "_" + i.get_name()))
                            output.write(modified_line.replace(mutation_headers[0], mutation_headers[0].replace(".h", "_" + i.get_name() + ".h")))

        sys.exit()
