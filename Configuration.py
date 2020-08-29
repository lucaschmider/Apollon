CONFIGURATION = {
    "TRIGGERS": {
        "DAILY_TRIGGER_TIME": (17, 30),
        "BUTTON_TRIGGER_PIN": 17
    },
    "CONSUMERS": {
        "SPEECH_CONSUMER": {"SERVICE_ACCOUNT_FILE": "../sa.json"}
    },
    "APPLICATION_HOOKS": {
        "LED": {
            "LED_COUNT": 20,
            "THEME": [(0, 0, 0), (0, 0, 255), (0, 162, 20), (255, 0, 0)],
            "ANIMATIONS": {
                "SPEECH": [
                    [1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 3, 3],
                    [2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 3, 3],
                    [2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 3, 3],
                    [2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 3, 3]
                ],
                "DEFAULT": [[2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 0, 0]],
                "GENERATING":[[0,0,0,0,0,0,0,0,0,0]]
            }
        }
    }

}
