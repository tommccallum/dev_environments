#include "version.hpp" // NOLINT  Generated by cmake
#include <fmt/color.h>
#include <fmt/format.h>
#include <iomanip>
#include <iostream>

constexpr int EXIT_CODE_ARG_ERROR = 2;
constexpr int EXIT_CODE_SUCCESS = 0;
const std::string APP_EXECUTABLE = "yourapp";

struct HelpOption
{
  std::string short_option;
  std::string long_option;
  std::string description;
};

struct UserSettings
{
};

const std::array<HelpOption, 1> help_options = {
    {{{"-h"}, {"--help"}, {"Print this help message.\n"}}}};

void print_help()
{
  fmt::print("Your application\n");
  fmt::print("\nUSAGE: ./app [options]\n");
  fmt::print("Provides functionality\n\n");
  for (auto opt : help_options)
  {
    fmt::print("  {:<4}{:<15}{}\n", opt.short_option, opt.long_option, opt.description);
  }
}

UserSettings parse_command_line_arguments(int num_arguments, char **argument_values)
{
  UserSettings settings;
  int ii = 1;
  while (ii < num_arguments)
  {
    auto option = std::string{argument_values[ii]};
    if (option == "-h" || option == "--help")
    {
      print_help();
      exit(EXIT_CODE_SUCCESS);
    }
    else
    {
      fmt::print("{0}: invalid option {1}\nTry './{0} --help' for more information.",
                 APP_EXECUTABLE,
                 argument_values[ii]);
      exit(EXIT_CODE_ARG_ERROR);
    }
    ii++;
  }
  return settings;
}

int main(int argc, char **argv)
{
  auto settings = parse_command_line_arguments(argc, argv);
  // do something
  (void) settings;
  return EXIT_CODE_SUCCESS;
}