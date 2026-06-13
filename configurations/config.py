import pathlib
import json
import yaml

class Config:
    """Loads Configuration files (.yaml and .json)

    Extracts information from loaded data files and passes them to other methods per requirement

    Examples:
        config = Config()
        config.get_test_product_id("adidas original")
    """

    #Set Path for Feature (Gherkin / Cucumber Feature)
    PATH_TO_FEATURE = pathlib.Path(__file__).parent.parent / "features"
    scenario_file = PATH_TO_FEATURE / "order_transaction.feature"

   #Set Path to Data Files
    PATH_TO_DATA = pathlib.Path(__file__).parent.parent / "data"
    json_config = PATH_TO_DATA / "credentials.json"
    yaml_config = PATH_TO_DATA / "config.yaml"
    test_data = PATH_TO_DATA / "test_data.yaml"

    with open(json_config, "r") as json_file:
        credentials = json.load(json_file)

    with open(yaml_config,"r") as yml_file:
        config = yaml.safe_load(yml_file)

    with open(test_data, "r", encoding="utf-8") as test_data:
        data_test = yaml.safe_load(test_data)

    def get_all_credentials(self) -> list[dict[str, str]]:
        """Grabs all  user credentials from credentials file (json).

        Returns:
            credentials["user_credentials"] (lst[dict]): List of user credentials
        """

        return self.credentials["user_credentials"]

    def get_credentials_main(self):
        """Grabs the main user credentials from file.

        The main user is defined as the one on index 0 of the users's list

        Returns:
            user_email (str): The user email used for login
            user_password (str): The user password used for login
        """
        user_email = self.credentials["user_credentials"][0]["email"]
        user_password = self.credentials["user_credentials"][0]["password"]
        return user_email, user_password

    def get_rahul_url_login(self) -> str:
        """Grabs the url address for the login page.

        Returns:
            self.config["webpages"]["rahul_login"] (str): Login page url
        """
        return self.config["webpages"]["rahul_login"]

    def get_api_baseurl(self):
        return self.config["api_base_urls"]["base_url"]

    def get_expected_cards(self):
        return self.data_test["dashboard"]["expected_cards"]

    def get_test_card_names(self):
        return self.data_test["dashboard"]["product_list"]

    def get_test_product_name(self, product_name:str):
        return self.data_test["order_details"][product_name.lower()]["name"]

    def get_test_product_price(self, product_name:str):
        return self.data_test["order_details"][product_name.lower()]["price"]

    def get_test_product_id(self, product_name:str):
        return self.data_test["order_details"][product_name.lower()]["itemid"]


if __name__ == "__main__":
    test = Config()
    email,password = test.get_credentials_main()
    print(f"{email},{password}")
    print(test.get_rahul_url_login())
    print(test.get_api_baseurl())
    print(test.get_all_credentials())
    print(test.get_expected_cards())
    print(test.get_test_card_names())
    print(test.get_test_product_name("adidas original"))
    print(test.get_test_product_price("adidas original"))
