from configparser import ConfigParser


class Config:

    file_path = "src/config/config.ini" 
    parser = ConfigParser()

    @classmethod
    def write_option_to_section(cls, section: str, option: str, value: str):
       cls.parser.read(cls.file_path)
       cls.parser.set(section, option, value)
       with open(cls.file_path, "w") as file:
           cls.parser.write(file)

    @classmethod
    def get_all_options_from_section(cls, section: str):
       cls.parser.read(cls.file_path)
       return cls.parser.options(section)


if __name__ == "__main__":
    Config.get_all_options_from_section("LOGIN_DETAILS")
