# jsonparse
Опис модуля:

Для роботи модуля необхідний json-файл.
Цей модуль отримує json-файл і дозволяє легко пересуватися по ньому і отримувати потрібні частини. 
Наприклад, при використанні модуля для файлу twiter1.json, програма буде виконуватися так:
```Enter the name of json file: "twitter1.json"
Choose one of the next keys in your json file:
1) users
2) next_cursor
3) next_cursor_str
4) previous_cursor
5) previous_cursor_str
6) total_count

Enter the key or press Enter to get a part of your json file: users // також можна ввести номер позиції
Next part of json file is a list. 
Please choose the number of list element: 0 - 19

Enter the key or press Enter to get a part of your json file:15
Choose one of the next keys in your json file:
1) id
2) id_str
3) name
4) screen_name
5) location
6) description
7) url
8) entities
9) protected
10) followers_count
11) friends_count
12) listed_count
13) created_at
14) favourites_count
15) utc_offset
16) time_zone
17) geo_enabled
18) verified
19) statuses_count
20) lang
21) status
22) contributors_enabled
23) is_translator
24) is_translation_enabled
25) profile_background_color
26) profile_background_image_url
27) profile_background_image_url_https
28) profile_background_tile
29) profile_image_url
30) profile_image_url_https
31) profile_banner_url
32) profile_link_color
33) profile_sidebar_border_color
34) profile_sidebar_fill_color
35) profile_text_color
36) profile_use_background_image
37) has_extended_profile
38) default_profile
39) default_profile_image
40) following
41) live_following
42) follow_request_sent
43) notifications
44) muting
45) blocking
46) blocked_by
47) translator_type

Enter the key or press Enter to get a part of your json file:1
users[15].id:   35112839```
