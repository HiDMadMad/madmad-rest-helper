"""
bot messages - multi-language support for telegram bot
"""

# emoji shortcuts
SLEEP_EMOJI = "💤"
CLOCK_EMOJI = "⏰"
MOON_EMOJI = "🌙"
SUN_EMOJI = "☀️"
INFO_EMOJI = "ℹ️"
BACK_EMOJI = "🔙"
LANG_EMOJI = "🌐"
CHECK_EMOJI = "✅"
CALCULATE_EMOJI = "🧮"
LIGHT_BULB_EMOJI = "💡"
SETTINGS_EMOJI = "⚙️"

MESSAGES = {
    "en": {
        # welcome & language
        "welcome": f"{SLEEP_EMOJI} welcome to Lehaam bot!\n\nplease select your language:",
        "language_selected": f"{CHECK_EMOJI} language set to English!",
        
        # main menu
        "main_menu": f"{SLEEP_EMOJI} *Lehaam - Sleep Optimizer*\n\nwhat would you like to do?",
        
        # buttons
        "btn_sleep_now": f"{MOON_EMOJI} sleep now",
        "btn_sleep_at": f"{CLOCK_EMOJI} sleep at HH:MM",
        "btn_wake_at": f"{SUN_EMOJI} wake up at HH:MM",
        "btn_about": f"{INFO_EMOJI} how it works",
        "btn_settings": f"{SETTINGS_EMOJI} settings",
        "btn_change_lang": f"{LANG_EMOJI} change language",
        "btn_back": f"{BACK_EMOJI} back to Menu",
        
        # sleep now
        "sleep_now_result": f"{MOON_EMOJI} *sleep now mode*\n\n"
                           f"current time: *{{}}:{{}}*\n\n"
                           f"if you go to sleep right now and fall asleep in 15 minutes,\n"
                           f"you should aim to wake up at:\n\n",
        
        # sleep at
        "sleep_at_prompt": f"{CLOCK_EMOJI} *sleep at specific time*\n\n"
                          f"when do you want to go to sleep?\n"
                          f"please send time in format: `HH:MM`\n\n"
                          f"example: `23:30` or `01:15`",
        
        "sleep_at_result": f"{CLOCK_EMOJI} *sleep at {{}}:{{}}*\n\n"
                          f"if you go to sleep at *{{}}:{{}}* and fall asleep in 15 minutes,\n"
                          f"you should aim to wake up at:\n\n",
        
        # wake at
        "wake_at_prompt": f"{SUN_EMOJI} *wake up at specific time*\n\n"
                         f"when do you want to wake up?\n"
                         f"please send time in format: `HH:MM`\n\n"
                         f"example: `07:00` or `08:30`",
        
        "wake_at_result": f"{SUN_EMOJI} *wake up at {{}}:{{}}*\n\n"
                         f"if you want to wake up refreshed at *{{}}:{{}}*,\n"
                         f"you should aim to go to sleep at:\n\n",
        
        # about - multiple sections
        "about_title": f"{INFO_EMOJI} *how Lehaam works*\n\nchoose a topic to learn more:",
        
        "about_cycles": f"{MOON_EMOJI} *sleep cycles explained*\n\n"
                       f"sleep happens in cycles of approximately *90 minutes*.\n\n"
                       f"each cycle has different stages:\n"
                       f"• Light Sleep (stage 1-2)\n"
                       f"• Deep Sleep (stage 3)\n"
                       f"• REM Sleep (dreaming)\n\n"
                       f"waking up *between cycles* (not during them) helps you feel more refreshed!",
        
        "about_timing": f"{CLOCK_EMOJI} *why timing matters*\n\n"
                       f"waking up in the middle of a deep sleep cycle makes you feel groggy and tired.\n\n"
                       f"but waking up between cycles makes you feel:\n"
                       f"• more alert and refreshed\n"
                       f"• more energized\n"
                       f"• ready to start your day\n\n"
                       f"Lehaam calculates the perfect times for you!",
        
        "about_calculation": f"{INFO_EMOJI} *how we calculate*\n\n"
                            f"Lehaam uses this formula :\n"
                            f"1. adds *15 minutes* (average time to fall asleep)\n"
                            f"2. adds multiples of *90 minutes* (sleep cycles)\n"
                            f"3. suggests *4-6 cycles* (6-9 hours) for optimal rest\n\n"
                            f"example : if you sleep at 23:00:\n"
                            f"• 23:00 + 15min = 23:15 (fall asleep)\n"
                            f"• 23:15 + 6×90min = 08:15 (wake up)\n"
                            f"this gives you 6 complete sleep cycles!",
        
        "about_tips": f"{CHECK_EMOJI} *sleep tips*\n\n"
                     f"for better sleep quality :\n"
                     f"• keep a consistent sleep schedule\n"
                     f"• avoid screens 1 hour before bed\n"
                     f"• keep your bedroom cool and dark\n"
                     f"• avoid caffeine 6 hours before sleep\n"
                     f"• exercise regularly (but not before bed)\n"
                     f"• create a relaxing bedtime routine",

        # settings
        "settings_menu": f"{SETTINGS_EMOJI} *settings*\n\ncustomize your experience:",
        "btn_timezone": "🌍 timezone offset",
        
        "timezone_prompt": f"🌍 *timezone offset*\n\nyour current offset: *{{}}*\n\nplease send your timezone offset in format:\n`+HH:MM` or `-HH:MM`\n\nexamples:\n• `+03:30` (Tehran)\n• `+04:00` (Dubai)\n\nor send `0` for UTC",
        
        "timezone_changed": f"{CHECK_EMOJI} timezone offset changed to *{{}}*!",
        "invalid_timezone": "❌ invalid timezone format!\n\nplease use format: `+HH:MM` or `-HH:MM`\nexample: `+03:30` or `-05:00`",
        
        # buttons for about section
        "btn_about_cycles": f"{MOON_EMOJI} sleep cycles",
        "btn_about_timing": f"{CLOCK_EMOJI} why timing matters",
        "btn_about_calc": f"{CALCULATE_EMOJI} how we calculate",
        "btn_about_tips": f"{LIGHT_BULB_EMOJI} sleep tips",
        
        # time format
        "time_format": "{}:{} {}",  # hour:minute (suggested/not)
        "suggested": "(⭐recommended)",
        "cycle_count": "• {} cycles ({}h {}m)",
        
        # errors
        "invalid_time": "❌ invalid time format!\n\nplease use format: `HH:MM`\nexample: `23:30` or `07:00`",
        "error_occurred": "❌ an error occurred. please try again or use /start",
        
        # other
        "cancel": "❌ cancelled. returning to main menu...",
    },
    
    "fa": {
        # welcome & language
        "welcome": f"{SLEEP_EMOJI} به لِهام خوش اومدی!\n\nلطفا زبانت رو انتخاب کن:",
        "language_selected": f"{CHECK_EMOJI} زبان به فارسی تغییر کرد!",
        
        # main menu
        "main_menu": f"{SLEEP_EMOJI} *لِهام - بهینه‌ساز خواب*\n\nچه کاری می‌خوای انجام بدی؟",
        
        # buttons
        "btn_sleep_now": f"{MOON_EMOJI} الان بخوابم",
        "btn_sleep_at": f"{CLOCK_EMOJI} ساعت خاصی بخوابم",
        "btn_wake_at": f"{SUN_EMOJI} ساعت خاصی بیدارشم",
        "btn_about": f"{INFO_EMOJI} چطور کار می‌کنه",
        "btn_change_lang": f"{LANG_EMOJI} تغییر زبان",
        "btn_back": f"{BACK_EMOJI} بازگشت به منو",
        
        # sleep now
        "sleep_now_result": f"{MOON_EMOJI} *الان بخوابی*\n\n"
                           f"زمان فعلی: *{{}}:{{}}*\n\n"
                           f"اگر الان بخوابی و در ۱۵ دقیقه به خواب بری،\n"
                           f"بهتره در این ساعت ها بیدار بشی:\n\n",
        
        # sleep at
        "sleep_at_prompt": f"{CLOCK_EMOJI} *خواب در ساعت خاص*\n\n"
                          f"میخوای چه ساعتی بخوابی؟\n"
                          f"لطفا زمان رو به فرمت `HH:MM` بفرست\n\n"
                          f"مثال: `23:30` یا `01:15`",
        
        "sleep_at_result": f"{CLOCK_EMOJI} *خواب در ساعت {{}}:{{}}*\n\n"
                          f"اگر ساعت *{{}}:{{}}* بخوابی و در ۱۵ دقیقه به خواب برو،\n"
                          f"بهتره در این ساعت ها بیدار بشی:\n\n",
        
        # wake at
        "wake_at_prompt": f"{SUN_EMOJI} *بیداری در ساعت خاص*\n\n"
                         f"میخوای چه ساعتی بیدار بشی؟\n"
                         f"لطفا زمان رو به فرمت `HH:MM` بفرست\n\n"
                         f"مثال: `07:00` یا `08:30`",
        
        "wake_at_result": f"{SUN_EMOJI} *بیداری در ساعت {{}}:{{}}*\n\n"
                         f"اگر میخوای ساعت *{{}}:{{}}* سرحال بیدار بشی،\n"
                         f"بهتره در این ساعت ها بخوابی:\n\n",
        
        # about - multiple sections
        "about_title": f"{INFO_EMOJI} *لِهام چطور کار می‌کنه؟*\n\nیک موضوع رو انتخاب کن:",
        
        "about_cycles": f"{MOON_EMOJI} *چرخه‌های خواب چیَن؟*\n\n"
                       f"خواب تو چرخه‌های تقریبا *۹۰ دقیقه‌ای* اتفاق می‌افته.\n\n"
                       f"هر چرخه مراحل مختلفی داره:\n"
                       f"• خواب سبک (مرحله ۱-۲)\n"
                       f"• خواب عمیق (مرحله ۳)\n"
                       f"• خواب REM (رویا دیدن)\n\n"
                       f"بیدار شدن *بین چرخه‌ها* (نه وسطشون) باعث میشه سرحال‌تر بیدار بشی!",
        
        "about_timing": f"{CLOCK_EMOJI} *چرا زمان‌بندی مهمه؟*\n\n"
                       f"بیدار شدن وسط یک چرخه خواب عمیق باعث می‌شه خسته و کسل بیدار بشی.\n\n"
                       f"اما بیدار شدن بین چرخه‌ها باعث میشه:\n"
                       f"• هوشیارتر و سرحال‌تر باشی\n"
                       f"• انرژی بیشتری داشته باشی\n"
                       f"• آماده شروع روز باشی\n\n"
                       f"لِهام بهترین زمان‌ها رو واست محاسبه می‌کنه!",
        
        "about_calculation": f"{INFO_EMOJI} *چطور محاسبه می‌کنیم؟*\n\n"
                            f"لِهام از این فرمول استفاده می‌کنه:\n\n"
                            f"۱. *۱۵ دقیقه* اضافه می‌کنه (زمان متوسط به خواب رفتن)\n"
                            f"۲. چند برابر *۹۰ دقیقه* اضافه می‌کنه (چرخه‌های خواب)\n"
                            f"۳. *۴ تا ۶ چرخه* (۶-۹ ساعت) رو پیشنهاد می‌ده\n\n"
                            f"مثال: اگر ساعت ۲۳:۰۰ بخوابی:\n"
                            f"• ۲۳:۰۰ + ۱۵ دقیقه = ۲۳:۱۵ (به خواب رفتن)\n"
                            f"• ۲۳:۱۵ + ۶×۹۰ دقیقه = ۰۸:۱۵ (بیدار شدن)\n"
                            f"این بهت ۶ چرخه کامل خواب می‌ده!",
        
        "about_tips": f"{CHECK_EMOJI} *نکات خواب بهتر*\n\n"
                     f"برای کیفیت بهتر خواب:\n\n"
                     f"• برنامه خواب منظم داشته باش\n"
                     f"• ۱ ساعت قبل خواب از صفحه نمایش دوری کن\n"
                     f"• اتاق خواب رو خنک و تاریک نگه دار\n"
                     f"• ۶ ساعت قبل خواب کافئین نخور\n"
                     f"• منظم ورزش کن (اما نه قبل خواب)\n"
                     f"• یک روال آرامش‌بخش قبل خواب داشته باش",

        # settings
        "settings_menu": f"{SETTINGS_EMOJI} *تنظیمات*\n\nتجربه‌ت رو شخصی‌سازی کن:",
        "btn_timezone": "🌍 اختلاف زمانی",
        
        "timezone_prompt": f"🌍 *اختلاف زمانی*\n\nاختلاف زمانی فعلی: *{{}}*\n\nلطفا اختلاف زمانی خودت رو به فرمت زیر بفرست:\n`+HH:MM` یا `-HH:MM`\n\nمثال‌ها:\n• `+03:30` (تهران)\n• `+04:00` (دبی)\n\nیا عدد `0` برای UTC",
        
        "timezone_changed": f"{CHECK_EMOJI} اختلاف زمانی به *{{}}* تغییر کرد!",
        "invalid_timezone": "❌ فرمت اشتباهه!\n\nلطفا از فرمت `+HH:MM` یا `-HH:MM` استفاده کن\nمثال: `+03:30` یا `-05:00`",
        
        # buttons for about section
        "btn_about_cycles": f"{MOON_EMOJI} چرخه‌های خواب",
        "btn_about_timing": f"{CLOCK_EMOJI} اهمیت زمان‌بندی",
        "btn_about_calc": f"{CALCULATE_EMOJI} نحوه محاسبه",
        "btn_about_tips": f"{LIGHT_BULB_EMOJI} نکات خواب",
        "btn_settings": f"{SETTINGS_EMOJI} تنظیمات",

        # time format
        "time_format": "{}:{} {}",
        "suggested": "(⭐ پیشنهادی)",
        "cycle_count": "• {} چرخه ({}ساعت و {}دقیقه)",

        # errors
        "invalid_time": "❌ فرمت زمان نادرسته!\n\nلطفا از فرمت `HH:MM` استفاده کن\nمثال: `23:30` یا `07:00`",
        "error_occurred": "❌ خطایی رخ داد. لطفا دوباره تلاش کن یا از /start استفاده کن",

        # other
        "cancel": "❌ لغو شد. بازگشت به منوی اصلی...",
    }
}

def get_message(lang:str, key:str) -> str:
    """get message in specified language"""
    return MESSAGES.get(lang, MESSAGES["en"]).get(key, "")

def format_time_result(lang:str, times:list, message_key:str, *args) -> str:
    """format sleep/wake times with language support"""
    msg = get_message(lang, message_key).format(*args) if args else get_message(lang, message_key)
    
    for time, suggested in times:
        time_str = f"*{time.hour:02d}:{time.minute:02d}*"
        if suggested:
            time_str += f" {get_message(lang, 'suggested')}"
        msg += f"{time_str}\n"
    
    return msg
#MadMad_253
