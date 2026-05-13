import pathlib
import json
import yaml

class Config:
   
    PATH = pathlib.Path("C:/Users/hp/Documents/FranciscoAlfonzo-Personal/Courses/Learning/Playwright-Rahul-Shetty-Course/data")
    json_config = PATH / "credentials.json"
    yaml_config = PATH / "config.yaml"

    with open(json_config, "r") as json_file:
        credentials = json.load(json_file)

    with open(yaml_config,"r") as yml_file:
        config = yaml.safe_load(yml_file)

    def get_all_credentials(self):
        return self.credentials["user_credentials"]

    def get_credentials_main(self):
        user_email = self.credentials["user_credentials"][0]["email"]
        user_password = self.credentials["user_credentials"][0]["password"]
        return user_email, user_password

    def get_rahul_url_login(self):
        return self.config["webpages"]["rahul_login"]

    def get_api_baseurl(self):
        return self.config["api_base_urls"]["base_url"]

if __name__ == "__main__":
    test = Config()
    email,password = test.get_credentials_main()
    print(f"{email},{password}")
    print(test.get_rahul_url_login())
    print(test.get_api_baseurl())
    print(test.get_all_credentials())