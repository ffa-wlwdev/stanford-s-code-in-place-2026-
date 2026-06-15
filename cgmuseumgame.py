import re
import sys
import time
import random

# =========================
# COLORED TEXT CONSTANTS
# =========================

BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"
RESET   = "\033[0m"


# =========================
# TEXT EFFECTS
# =========================

def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def cinematic_print(text, sentence_delay=1.0, char_delay=0.0):
    paragraphs = text.strip().split("\n")

    for para in paragraphs:
        para = para.strip()

        if not para:
            print()
            continue

        # Apply color tags to the full paragraph before splitting
        para_colored = colorize(para)

        # Split into sentences safely
        sentences = re.split(r'(?<=[.!?])\s+', para_colored)

        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue

            if char_delay > 0:
                for char in sentence:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(char_delay)
                print()
            else:
                print(sentence)

            time.sleep(sentence_delay)

        print()  # space after each paragraph


def reveal(text, delay=1.0):
    print(text)
    time.sleep(delay)


def colorize(text):
    return text.replace("[RED]", RED).replace("[RESET]", RESET)


# =========================
# TITLE SCREEN
# =========================

def title():
    print()

    lines = [
        "=" * 35,
        " | ONE NIGHT AT THE C.G. MUSEUM |",
        "=" * 35
    ]

    for line in lines:
        print(f"{GREEN}{line}{RESET}")
        time.sleep(0.2)

    print()


# =========================
# INTRO
# =========================

def intro():
    print("* This is a console game — use the full terminal.")
    print("* Read the text carefully and type answers exactly as shown.\n")

    while True:
        start = input(MAGENTA + "* Start Game { Y/N } : " + RESET).upper().strip()
        if start == "Y":
            return True
        elif start == "N":
            print("Game exited.")
            return False
        else:
            print(RED + "Please enter Y or N." + RESET)


# =========================
# STORY
# =========================

def story():
    print("\n" + CYAN + "THE TALE" + RESET)
    print(CYAN + "-" * 35 + RESET)
    print()

    cinematic_print(
        "During World War II, an enigmatic opportunity arrived unexpectedly for the women of America. "
        "Over ten thousand young women were recruited by the U.S. Army and Navy to serve as codebreakers.\n\n"
        "They would go on to make history.\n\n"
        "You are here to learn about these women's stories — and it is your job to ensure history does not change tonight.\n\n"
        "Some [RED]enigmatic rogues[RESET] have been scheming to steal from the Museum and destroy its records before the Annual Exhibition.\n\n"
        "With full security in the shadows, there are three people scouting the Museum tonight — including you."
    )

    input(MAGENTA + "* Press Enter to continue..." + RESET)


# =========================
# CHARACTERS
# =========================

def meet_characters():
    print("\n" + CYAN + "MEET THE CHARACTERS" + RESET)
    print("-" * 35 + "\n")

    reveal(
        GREEN + "1. Detective Meyer Driscoll | Game-Mode: Cipher Decrypting" + RESET
    )
    reveal(
        "Decrypt the 5 strange messages left by the Enigmatic Rogues. "
        "What are they trying to communicate? Can you trace their steps and "
        "find out where they are going next? Let's try to catch them in time."
    )
    reveal(GREEN + "Difficulty: Medium" + RESET)
    print()

    reveal(
        YELLOW + "2. Museum Curator Helen Aderholt | Game-Mode: Trivia, Multiple Choice" + RESET
    )
    reveal(
        "Walk through the corridors and restore the 5 placards that have been left distorted. "
        "You may not have access to external resources, "
        "but you have one brilliant thing the Enigmatic Rogues can't take from you: Your mind!"
    )
    reveal(YELLOW + "Difficulty: Easy" + RESET)
    print()

    reveal(
        MAGENTA + "3. Hacker PURPLE_CIPHER | Game-Mode: Cipher & Trivia, No Hints" + RESET
    )
    reveal(
        "To catch the Enigmatic Rogues, you must first think like them. "
        "Operating from the Museum's security room, your resources and time are limited. "
        "You need the 3 remaining puzzle pieces to track them down and restore the museum records."
    )
    reveal(MAGENTA + "Difficulty: Advanced" + RESET)
    print()

    reveal("* For BEGINNERS, Detective or Curator is recommended!")
    reveal("* For RISK-TAKERS, try the Hacker mode!")

    input(MAGENTA + "\n* Press Enter to proceed to the Selection Menu..." + RESET)


# =========================
# DETECTIVE TUTORIAL
# =========================

def detective_tutorial():
    print("\n" + CYAN + "DETECTIVE BRIEFING" + RESET)
    print("-" * 35 + "\n")

    cinematic_print(
        "Before you begin, you review the basics of the cipher used in the museum.\n\n"
        "The Enigmatic Rogues are using a Caesar Cipher with a fixed shift.\n"
        "Each letter is moved forward in the alphabet by a key value.\n\n"
        "To decrypt, you reverse the process: shift letters BACK by the same key.\n\n"
        "Example:\n"
        "KAREL shifted +3 becomes NDUHO.\n"
        "So NDUHO shifted back -3 becomes KAREL again.\n\n"
        "This method is one of the earliest forms of cryptography — simple, but historically important.\n\n"
        "During World War II, thousands of women known as the Code Girls worked as U.S. Army and Navy codebreakers.\n"
        "Their work helped decode encrypted enemy communications and shaped wartime intelligence.\n\n"
        "The shift key used by the Enigmatic Rogues is: [RED]+3[RESET] (decrypt by shifting back 3)."
    )

    print(YELLOW + "\nOptional reading (open in your browser for more context):" + RESET)
    print(CYAN + "https://samantha-allen.github.io/Documents/CodeGirls1.pdf" + RESET)

    input(MAGENTA + "\n* Press Enter to begin the investigation..." + RESET)


# =========================
# MURDER BOARD
# =========================

murder_board = {
    "HOW MANY ROGUES ARE THERE?": "UNKNOWN",
    "WHAT ARE THEIR NAMES?":       "UNKNOWN",
    "WHY ARE THEY DOING THIS?":    "UNKNOWN",
    "WHEN DID THEY BREAK IN?":     "UNKNOWN",
    "WHERE ARE THEY GOING NEXT?":  "UNKNOWN"
}

puzzles = [
    {
        "cipher": "WKUHH",
        "answer": "THREE",
        "board_key": "HOW MANY ROGUES ARE THERE?",
        "board_value": "THREE",
        "hint_q": "Which of these is NOT a base command in the Karel program?\nA) move()\nB) turn_left()\nC) place_beeper()\nD) pick_beeper()",
        "hint_answer": "C",
        "hint_explanation": "Karel only has four base commands: move(), turn_left(), pick_beeper(), and put_beeper(). 'place_beeper()' does not exist.",
        "cipher_explanation": "Caesar shift -3:  W→T, K→H, U→R, H→E, H→E  →  THREE",
        "hint_wrong": {
            "A": "move() IS a valid Karel command — it moves Karel one step forward.",
            "B": "turn_left() IS valid — Karel can only turn left natively.",
            "D": "pick_beeper() IS valid — Karel picks up a beeper from the current cell."
        }
    },
    {
        "cipher": "CDQQ, GDUH, QDRM",
        "answer": "ZANN, DARE, NAOJ",
        "board_key": "WHAT ARE THEIR NAMES?",
        "board_value": "ZANN, DARE, NAOJ",
        "hint_q": "How does Python define a block of code?\nA) Semicolons\nB) Indentation\nC) Curly Brackets\nD) All of the above",
        "hint_answer": "B",
        "hint_explanation": "Python uses indentation (whitespace) to define code blocks — unlike most languages that use braces or brackets.",
        "cipher_explanation": "Shift -3 each letter:  C→Z, D→A, Q→N, Q→N  →  ZANN | G→D, D→A, U→R, H→E  →  DARE | Q→N, D→A, R→O, M→J  →  NAOJ",
        "hint_wrong": {
            "A": "Semicolons end statements in some languages (like C or Java), but Python doesn't require them for blocks.",
            "C": "Curly brackets {} are used in languages like Java or C++, not Python.",
            "D": "Python only uses indentation — the other options don't apply."
        }
    },
    {
        "cipher": "KLUHG EB ULYDOV",
        "answer": "HIRED BY RIVALS",
        "board_key": "WHY ARE THEY DOING THIS?",
        "board_value": "HIRED BY RIVALS",
        "hint_q": "Who created Karel the Robot?\nA) Adele Goldberg\nB) James Gosling\nC) Shafi Goldwasser\nD) Richard E. Pattis",
        "hint_answer": "D",
        "hint_explanation": "Richard E. Pattis created Karel the Robot at Stanford University in 1981, naming it after Czech playwright Karel Čapek.",
        "cipher_explanation": "Shift -3:  K→H, L→I, U→R, H→E, G→D  →  HIRED | E→B, B→Y  →  BY | U→R, L→I, Y→V, D→A, O→L, V→S  →  RIVALS",
        "hint_wrong": {
            "A": "Adele Goldberg was a key contributor to Smalltalk at Xerox PARC.",
            "B": "James Gosling created Java.",
            "C": "Shafi Goldwasser is a pioneering cryptographer, not Karel's creator."
        }
    },
    {
        "cipher": "GXVN",
        "answer": "DUSK",
        "board_key": "WHEN DID THEY BREAK IN?",
        "board_value": "DUSK",
        "hint_q": "Which of these is NOT a Python core built-in data type?\nA) Tuple\nB) List\nC) Class\nD) Dictionary",
        "hint_answer": "C",
        "hint_explanation": "Class is a user-defined construct in Python — not a built-in data type. The four core built-in collection types are list, tuple, set, and dictionary.",
        "cipher_explanation": "Shift -3:  G→D, X→U, V→S, N→K  →  DUSK",
        "hint_wrong": {
            "A": "Tuple IS a core Python type — an immutable ordered collection.",
            "B": "List IS a core Python type — a mutable ordered collection.",
            "D": "Dictionary IS a core Python type — stores key-value pairs."
        }
    },
    {
        "cipher": "GRZQWRZQ",
        "answer": "DOWNTOWN",
        "board_key": "WHERE ARE THEY GOING NEXT?",
        "board_value": "DOWNTOWN",
        "hint_q": "What is the output of 'a' + 'bc' in Python?\nA) bc\nB) abc\nC) a\nD) bca",
        "hint_answer": "B",
        "hint_explanation": "The + operator concatenates strings in Python. 'a' + 'bc' joins them in order, producing 'abc'.",
        "cipher_explanation": "Shift -3:  G→D, R→O, Z→W, Q→N, W→T, R→O, Z→W, Q→N  →  DOWNTOWN",
        "hint_wrong": {
            "A": "'bc' alone would only be the second string — the + joins both.",
            "C": "'a' alone is just the first string, before concatenation.",
            "D": "'bca' would imply the second string comes first — that's not how + works."
        }
    }
]


def show_board():
    print("\n" + "=" * 44)
    print(RED + "   MURDER BOARD — THE ENIGMATIC ROGUES" + RESET)
    print("=" * 44)
    for k, v in murder_board.items():
        status = GREEN + v + RESET if v != "UNKNOWN" else YELLOW + v + RESET
        print(f"  {k}\n    → {status}")
    print("=" * 44 + "\n")


# =========================
# HINT MODE
# =========================

def hint_mode(question, correct_letter, explanation, cipher_answer, cipher_explanation, wrong_map):
    print("\n" + CYAN + "— HINT CHALLENGE —" + RESET)
    print(YELLOW + question + RESET)

    while True:
        user = input("\nYour answer (A/B/C/D) or type SOL for full solution: ").upper().strip()

        if user == correct_letter:
            print(GREEN + "\nCorrect! Hint unlocked." + RESET)
            print(YELLOW + "\nWhy this is correct:" + RESET)
            print(explanation)

            if wrong_map:
                print(CYAN + "\nWhy the other options are wrong:" + RESET)
                for key, reason in wrong_map.items():
                    if key != correct_letter:
                        print(f"  {key}) {reason}")

            print(CYAN + "\nCipher connection:" + RESET)
            print(cipher_explanation)
            print(YELLOW + f"\nDecrypted answer: {cipher_answer}" + RESET)
            return

        elif user == "SOL":
            print(CYAN + "\n— FULL HINT SOLUTION —" + RESET)
            print(YELLOW + "\nCorrect answer & explanation:" + RESET)
            print(explanation)

            if wrong_map:
                print(CYAN + "\nAll option breakdown:" + RESET)
                for key, reason in wrong_map.items():
                    print(f"  {key}) {reason}")

            print(CYAN + "\nCipher breakdown:" + RESET)
            print(cipher_explanation)
            print(YELLOW + f"\nDecrypted cipher answer: {cipher_answer}" + RESET)
            return

        else:
            print(RED + "Incorrect. Try again, or type SOL to reveal the full solution." + RESET)


# =========================
# CIPHER GAME (DETECTIVE)
# =========================

def cipher_game():
    show_board()

    print("\n" + GREEN + "CASE FILE: ENIGMATIC ROGUES INVESTIGATION" + RESET)
    print("-" * 50)
    print(CYAN + "Shift key: each letter was encrypted by +3. Decrypt by shifting back 3." + RESET)
    print(CYAN + "Commands: type your answer | HINT (CS trivia clue) | CLUE (full reveal)\n" + RESET)

    for puzzle in puzzles:

        while True:
            print(YELLOW + f"\n[ ENCRYPTED MESSAGE ]: {puzzle['cipher']}" + RESET)

            choice = input("Your answer / HINT / CLUE: ").upper().strip()

            if choice == puzzle["answer"]:
                print(GREEN + "\nCorrect! Clue recorded to the board.\n" + RESET)
                murder_board[puzzle["board_key"]] = puzzle["board_value"]
                show_board()
                break

            elif choice == "HINT":
                hint_mode(
                    puzzle["hint_q"],
                    puzzle["hint_answer"],
                    puzzle["hint_explanation"],
                    puzzle["answer"],
                    puzzle["cipher_explanation"],
                    puzzle.get("hint_wrong", {})
                )
                # After hint, player still needs to enter the cipher answer
                print(CYAN + f"\nNow try decrypting: {puzzle['cipher']}" + RESET)

            elif choice == "CLUE":
                print(CYAN + "\n— FULL DECRYPTION UNLOCKED —" + RESET)
                print(f"  Cipher:  {puzzle['cipher']}")
                print(f"  Answer:  {puzzle['answer']}")
                print(f"  How:     {puzzle['cipher_explanation']}")
                print(YELLOW + "\nType the answer above to continue." + RESET)

            elif choice == "":
                print(RED + "Please type an answer, HINT, or CLUE." + RESET)

            else:
                print(RED + "Incorrect. Try again, or type HINT for a clue / CLUE for the full reveal." + RESET)

    return end_scene()


# =========================
# CURATOR MODE
# =========================

def curator_mode():
    print("\n" + YELLOW + "MUSEUM CURATOR MODE: PLACARD RESTORATION" + RESET)
    print("-" * 55)

    cinematic_print(
        "You peruse your notes as you set down to restore the besmirched placards.\n"
        "The Enigmatic Rogues have tampered with five historical displays.\n"
        "It falls to you, Curator Helen Aderholt, to set the record straight."
    )

    while True:
        choice = input(
            CYAN + "\nWould you like to open your research notes? (Y/N): " + RESET
        ).upper().strip()

        if choice == "Y":
            print(YELLOW + "\nOpening archival reference...\n" + RESET)
            print(CYAN + "https://en.wikipedia.org/wiki/Code_Girls" + RESET)
            print("(Open this link in your browser for background reading)\n")
            break
        elif choice == "N":
            print(YELLOW + "\nVery well. Trusting your memory...\n" + RESET)
            break
        else:
            print(RED + "Please enter Y or N." + RESET)

    trivia_board = {
        "I":   None,
        "II":  None,
        "III": None,
        "IV":  None,
        "V":   None
    }

    trivia = [
        {
            "q": (
                "PLACARD I\n"
                "Which famous female cryptanalyst helped lay the early groundwork\n"
                "for U.S. codebreaking before and during WWII?\n"
                "  A) Virginia Dare Aderholdt\n"
                "  B) Agnes Meyer Driscoll\n"
                "  C) Helen Nibouar"
            ),
            "a": "B",
            "key": "I",
            "value": "Agnes Meyer Driscoll — Pioneer U.S. Cryptanalyst",
            "hint_q": "What is the name of the Detective character in this game?\n  A) Virginia\n  B) Agnes\n  C) Helen",
            "hint_answer": "B",
            "hint_explanation": (
                "Detective Meyer Driscoll is named after Agnes Meyer Driscoll — "
                "a real cryptanalyst who worked for the U.S. Navy and cracked multiple Japanese cipher systems."
            )
        },
        {
            "q": (
                "PLACARD II\n"
                "What was one of the key breakthroughs achieved by Genevieve Grotjan Feinstein?\n"
                "  A) Designing the Enigma machine\n"
                "  B) Identifying patterns in the Japanese Purple cipher\n"
                "  C) Developing radar technology"
            ),
            "a": "B",
            "key": "II",
            "value": "Genevieve Grotjan Feinstein — Cracked Purple Cipher Patterns",
            "hint_q": "What word is in the Hacker character's name?\n  A) Driscoll\n  B) PURPLE\n  C) Feinstein",
            "hint_answer": "B",
            "hint_explanation": (
                "The Hacker is called PURPLE_CIPHER — a nod to Genevieve Grotjan Feinstein, "
                "who identified the cyclical patterns in Japan's Purple cipher system in 1940, working for the U.S. Army SIS."
            )
        },
        {
            "q": (
                "PLACARD III\n"
                "What nickname is used for the WWII women codebreakers?\n"
                "  A) Cipher Sisters\n"
                "  B) Code Girls\n"
                "  C) Signal Maidens"
            ),
            "a": "B",
            "key": "III",
            "value": "The Code Girls — WWII Women Codebreakers",
            "hint_q": "What does C.G. stand for in the Museum name?\n  A) Cipher Group\n  B) Code Girls\n  C) Control Group",
            "hint_answer": "B",
            "hint_explanation": (
                "The Museum is called the C.G. Museum — C.G. stands for Code Girls, "
                "the popular name for the over 10,000 women who served as WWII codebreakers."
            )
        },
        {
            "q": (
                "PLACARD IV\n"
                "Why were Code Girls primarily recruited from colleges?\n"
                "  A) Strong math and language skills\n"
                "  B) Engineering backgrounds\n"
                "  C) Political science training"
            ),
            "a": "A",
            "key": "IV",
            "value": "Recruited for Mathematics and Modern Languages",
            "hint_q": "Which subjects were valued most in codebreaking?\n  A) Math and languages\n  B) Engineering\n  C) Political science",
            "hint_answer": "A",
            "hint_explanation": (
                "Cryptanalysis requires pattern recognition (math) and linguistic understanding. "
                "Recruiters specifically looked for women with strong mathematics and foreign language backgrounds."
            )
        },
        {
            "q": (
                "PLACARD V\n"
                "What was the primary function of the Code Girls during WWII?\n"
                "  A) Translating intercepted messages\n"
                "  B) Operating military radio equipment\n"
                "  C) Performing cryptanalysis on enemy communications"
            ),
            "a": "C",
            "key": "V",
            "value": "Cryptanalysis — Decoding Enemy Naval Communications",
            "hint_q": "Which military branch relied most heavily on Code Girls?\n  A) Army\n  B) Navy\n  C) Air Force",
            "hint_answer": "B",
            "hint_explanation": (
                "The U.S. Navy recruited the largest number of Code Girls and relied on them "
                "to decrypt Japanese and German naval communications throughout the war."
            )
        }
    ]

    for item in trivia:
        while True:
            print(YELLOW + "\n" + item["q"] + RESET)

            user = input("\nYour answer (A/B/C) / HINT / CLUE: ").upper().strip()

            if user == item["a"]:
                print(GREEN + "\nCorrect! Placard restored.\n" + RESET)
                trivia_board[item["key"]] = item["value"]
                break

            elif user == "HINT":
                hint_mode(
                    item["hint_q"],
                    item["hint_answer"],
                    item["hint_explanation"],
                    item["a"],
                    item["hint_explanation"],
                    {}
                )
                print(CYAN + "\nNow try answering the placard question above." + RESET)

            elif user == "CLUE":
                print(CYAN + "\n— FULL RESTORATION UNLOCKED —" + RESET)
                print(GREEN + f"Answer: {item['value']}" + RESET)
                trivia_board[item["key"]] = item["value"]
                break

            elif user == "":
                print(RED + "Please type A, B, C, HINT, or CLUE." + RESET)

            else:
                print(RED + "Incorrect. Try again, or type HINT for a clue / CLUE to reveal." + RESET)

        # Show restored board so far
        print(CYAN + "\n— RESTORED PLACARDS SO FAR —" + RESET)
        for k, v in trivia_board.items():
            if v:
                print(f"  {k}: {GREEN}{v}{RESET}")
            else:
                print(f"  {k}: {YELLOW}(pending){RESET}")

    print("\n" + CYAN + "=" * 44 + RESET)
    print(CYAN + "     MUSEUM RESTORATION COMPLETE" + RESET)
    print(CYAN + "=" * 44 + RESET)

    cinematic_print(
        "Every placard has been restored.\n"
        "The museum's history shines once again with clarity and truth.\n\n"
        "You have successfully preserved the legacy of the Code Girls.\n"
        "Their stories — once threatened — will endure for every visitor who walks through these halls."
    )

    while True:
        nxt = input(
            MAGENTA + "\nCurious whether the Detective caught the Enigmatic Rogues? (Y/N): " + RESET
        ).upper().strip()

        if nxt == "Y":
            roleSelectFlow()
            return
        elif nxt == "N":
            quit_game()
            return
        else:
            print(RED + "Please enter Y or N." + RESET)


# =========================
# HACKER MODE
# =========================

def hacker_mode():
    print("\n" + MAGENTA + "SECURITY ROOM ACCESS GRANTED: HACKER MODE" + RESET)
    print("-" * 60)

    cinematic_print(
        "You sit inside the Museum's dimly lit security room.\n"
        "Monitors flicker. Archived footage loops in the background.\n"
        "Somewhere in the system, the Enigmatic Rogues are still active...\n\n"
        "But this time, you're not solving clues step-by-step.\n"
        "You're breaking through everything at once — no hints, no safety net.\n\n"
        "The shift key is [RED]+3[RESET]. Decrypt by reversing.\n"
        "Three system nodes stand between you and the truth."
    )

    input(MAGENTA + "\n* Press Enter to begin the breach sequence..." + RESET)

    # -------------------------
    # COMBINED PUZZLE POOL
    # -------------------------

    pool = []

    for p in puzzles:
        pool.append({
            "type": "CIPHER",
            "q": f"Decrypt this message (Caesar shift -3):\n  {p['cipher']}",
            "a": p["answer"]
        })

    trivia_questions = [
        {
            "type": "TRIVIA",
            "q": (
                "Which female cryptanalyst helped lay early U.S. codebreaking foundations?\n"
                "  A) Virginia Dare Aderholdt\n"
                "  B) Agnes Meyer Driscoll\n"
                "  C) Helen Nibouar"
            ),
            "a": "B"
        },
        {
            "type": "TRIVIA",
            "q": (
                "Key breakthrough by Genevieve Grotjan Feinstein?\n"
                "  A) Enigma design\n"
                "  B) Cracking Purple cipher patterns\n"
                "  C) Radar technology"
            ),
            "a": "B"
        },
        {
            "type": "TRIVIA",
            "q": (
                "Nickname for WWII women codebreakers?\n"
                "  A) Cipher Sisters\n"
                "  B) Code Girls\n"
                "  C) Signal Maidens"
            ),
            "a": "B"
        },
        {
            "type": "TRIVIA",
            "q": (
                "Why were Code Girls recruited from colleges?\n"
                "  A) Math & languages\n"
                "  B) Engineering\n"
                "  C) Political science"
            ),
            "a": "A"
        },
        {
            "type": "TRIVIA",
            "q": (
                "Primary function of Code Girls in WWII?\n"
                "  A) Translating messages\n"
                "  B) Radio operations\n"
                "  C) Cryptanalysis"
            ),
            "a": "C"
        }
    ]

    pool.extend(trivia_questions)

    # Randomly pick 3 unique challenges
    selected = random.sample(pool, 3)

    solved = 0

    for i, item in enumerate(selected, 1):
        while True:
            print("\n" + MAGENTA + f"[ SYSTEM NODE {i} ] — TYPE: {item['type']}" + RESET)
            print(YELLOW + item["q"] + RESET)

            user = input("\nANSWER (or BACK to return to role select): ").upper().strip()

            if user == "BACK":
                print(CYAN + "\nDisconnecting from security system..." + RESET)
                roleSelectFlow()
                return

            elif user == "":
                print(RED + "Please enter an answer or BACK." + RESET)

            elif user == item["a"]:
                print(GREEN + "ACCESS GRANTED. NODE BREACHED.\n" + RESET)
                solved += 1
                break

            else:
                print(RED + "ACCESS DENIED. Incorrect answer. Try again or type BACK." + RESET)

    # -------------------------
    # ENDING
    # -------------------------

    print("\n" + CYAN + "=" * 50 + RESET)
    print(CYAN + "        SECURITY OVERRIDE COMPLETE" + RESET)
    print(CYAN + "=" * 50 + RESET)

    cinematic_print(
        "All systems breached.\n"
        "The Enigmatic Rogues' final trace has been located and neutralised.\n\n"
        "But something unexpected surfaces...\n\n"
        "You, the Hacker known as PURPLE_CIPHER, were never just chasing criminals...\n"
        "You were building something better, aiming for something higher, more ambitious.\n\n"
        "Your rival in the shadows, the Enigmatic Rogues: Now exposed.\n\n"
        "And now — you are a protector of the Code Girls Museum archives.\n"
        "A newly appointed white-hat security specialist, putting your hacking skills and swift thinking to good use.\n"
    )

    while True:
        nxt = input(
            MAGENTA + "\nWould you like to explore the other perspectives of the case in depth? (Y/N): " + RESET
        ).upper().strip()

        if nxt == "Y":
            roleSelectFlow()
            return
        elif nxt == "N":
            quit_game()
            return
        else:
            print(RED + "Please enter Y or N." + RESET)


# =========================
# ROLE SELECT
# =========================

def start_role(role):
    if role == "1":
        print(GREEN + "\nYou selected Detective Meyer Driscoll!" + RESET)
        detective_tutorial()
        result = cipher_game()
        if result == "Y":
            roleSelectFlow()
        else:
            quit_game()

    elif role == "2":
        print(YELLOW + "\nYou selected Curator Helen Aderholt!" + RESET)
        curator_mode()

    elif role == "3":
        print(MAGENTA + "\nYou selected Hacker PURPLE_CIPHER!" + RESET)
        hacker_mode()


def roleSelect():
    while True:
        print("\n" + CYAN + "— SELECT YOUR ROLE —" + RESET)
        print("  * 1. Detective (Cipher Decryption)")
        print("  * 2. Curator   (Historical Trivia)")
        print("  * 3. Hacker    (Cipher + Trivia, No Hints)")
        print("\n  Select a game mode: {1} | {2} | {3}")
        print("  Type X to review character information")

        choice = input("\nSelection: ").upper().strip()

        if choice in ["1", "2", "3"]:
            return choice
        elif choice == "X":
            meet_characters()
        elif choice == "":
            print(RED + "Please enter 1, 2, 3, or X." + RESET)
        else:
            print(RED + "Invalid input. Enter 1, 2, 3, or X." + RESET)


def roleSelectFlow():
    role = roleSelect()
    start_role(role)


# =========================
# END SCENE (DETECTIVE)
# =========================

def end_scene():
    print("\n" + CYAN + "=" * 44 + RESET)
    print(CYAN + "              CASE CLOSED" + RESET)
    print(CYAN + "=" * 44 + RESET)

    cinematic_print(
        "All five encrypted messages have been decoded.\n\n"
        "The Enigmatic Rogues were intercepted downtown before they could escape.\n"
        "Museum security recovered every stolen artifact and returned them safely "
        "ahead of the Annual Exhibition.\n\n"
        "History remains intact — for now.\n"
    )

    while True:
        choice = input(
            MAGENTA + "\nWould you like to see how Curator Aderholt is restoring the museum displays? (Y/N): " + RESET
        ).upper().strip()

        if choice == "Y":
            return "Y"
        elif choice == "N":
            return "N"
        else:
            print(RED + "Please enter Y or N." + RESET)


# =========================
# QUIT
# =========================

def quit_game():
    print("\n" + CYAN + "THANK YOU FOR PLAYING!" + RESET)
    print("=" * 40)

    cinematic_print(
        "The museum lights dim as the night comes to an end.\n"
        "Your work tonight preserved history and protected the legacy of the Code Girls.\n\n"
        "Thanks for stepping into the investigation."
    )

    print(GREEN + "\nGoodbye.\n" + RESET)
    raise SystemExit(0)


# =========================
# MAIN
# =========================

def main():
    print(CYAN + "\n## Presented by: Yours Truly | Stanford | Code in Place | 2026 ##" + RESET)

    title()

    if not intro():
        return

    story()

    meet_characters()

    roleSelectFlow()


if __name__ == "__main__":
    main()