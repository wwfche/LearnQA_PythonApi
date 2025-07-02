import requests
import pytest

class TestUserAgent:
    test_data = [
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
         "CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
         "Mobile", "Chrome", "iOS"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
         "Chrome/91.0.4472.124 Safari/537.36",
         "Web", "Chrome", "Unknown"),
        ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
         "Chrome/89.0.4389.114 Safari/537.36",
         "Web", "Chrome", "Unknown"),
        ("Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/605.1.15 "
         "(KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",
         "Mobile", "Safari", "iOS"),
        ("Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) "
         "Chrome/83.0.4103.106 Mobile Safari/537.36",
         "Mobile", "Chrome", "Android"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
         "Web", "Unknown", "Unknown"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
         "Edg/91.0.864.59",
         "Web", "Unknown", "Unknown"),
        ("Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) "
         "Chrome/62.0.3202.84 Mobile Safari/537.36",
         "Mobile", "Chrome", "Android"),
        ("Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 "
         "(KHTML, like Gecko) Mobile/15E148",
         "Mobile", "Safari", "iOS"),
        ("Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
         "Web", "Unknown", "Unknown"),
    ]

    @pytest.mark.parametrize("user_agent, expected_platform, expected_browser, expected_device", test_data)
    def test_user_agent_check(self, user_agent, expected_platform, expected_browser, expected_device):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        response = requests.get(url, headers={"User-Agent": user_agent})
        data = response.json()

        platform = data.get("platform")
        browser = data.get("browser")
        device = data.get("device")

        mismatches = []
        if platform != expected_platform:
            mismatches.append(f"platform: expected '{expected_platform}', got '{platform}'")
        if browser != expected_browser:
            mismatches.append(f"browser: expected '{expected_browser}', got '{browser}'")
        if device != expected_device:
            mismatches.append(f"device: expected '{expected_device}', got '{device}'")

        if mismatches:
            print(f"\nUser-Agent: {user_agent}")
            for mismatch in mismatches:
                print("  " + mismatch)

        assert not mismatches, "User-Agent дал неверные значения"
