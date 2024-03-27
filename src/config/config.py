import os
from configparser import ConfigParser


class Config:

    class Section:

        LOGIN_DETAILS = "LOGIN_DETAILS"
        SCRAPE_SETTINGS = "SCRAPE_SETTINGS"

    file_path = "src/config/config.ini" 
    parser = ConfigParser()

    # Create file.
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            pass

    # Create sections.
    sections_to_add = [Section.LOGIN_DETAILS, Section.SCRAPE_SETTINGS]
    for section in sections_to_add:
        if not parser.has_section(section):
            parser.add_section(section)
    with open(file_path, "w") as file:
        parser.write(file)

    @classmethod
    def write_option_to_section(cls, section: str, option: str, value: str):
       cls.parser.read(cls.file_path)
       cls.parser.set(section, option, value)
       with open(cls.file_path, "w") as file:
           cls.parser.write(file)

    @classmethod
    def get_all_options_from_section(cls, section: str):
       cls.parser.read(cls.file_path)
       return dict(cls.parser.items(section))

    @classmethod
    def delete_all_options_from_section(cls, section: str):
       cls.parser.read(cls.file_path)
       options = cls.parser.options(section)
       for option in options:
           cls.parser.remove_option(section, option)
       with open(cls.file_path, "w") as file:
           cls.parser.write(file)


if __name__ == "__main__":
    print(Config.get_all_options_from_section(Config.Section.SCRAPE_SETTINGS))
