import allure
class TestLogin:
    @allure.step('不知道')
    def test_a(self):
        print(000)
        allure.attach('1111', '1111111111111')
        print(111)
        allure.attach('22222', '22222222222222')
        assert 1

    @allure.step('登录步骤描述')
    def test_b(self):
        print(2222)
        allure.attach('number 1', '我是测试步骤001的描述～～～')
        print(3333)
        allure.attach('number 2', '我是测试步骤002的描述～～～')
        assert 0

