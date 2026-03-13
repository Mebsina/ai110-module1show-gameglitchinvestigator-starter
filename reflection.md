# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    - The game looks like a standard number guesser at first glance. Visually, it features a title, a difficulty selector, an input field, and a submit button. However, the functionality breaks immediately upon use.
      - Despite the prompt to choose a number between 1 and 100, I tested the input with a 0 against the actual target number, 17, the game still provided the hint to "Go LOWER!"
      - The user interface is also unresponsive to standard keyboard commands. Although the on-screen instruction explicitly says to "Press Enter to submit form," the Enter key does nothing. I had to manually click the submit button to proceed.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  - Enter key not submitting the form 
  - Hints were backwards

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - One example of a correct AI suggestion was the recommendation to use a Streamlit form to fix the unresponsive `Enter` key. The problem was that pressing `Enter` in a standard input field did not trigger the submission logic, forcing me to click the button manually every time.
  - The AI suggested wrapping the input field and the submit button within an `st.form` block. I verified the fix by testing the `Enter` key specifically. After the change, the key automatically mapped to the submit button, allowing the game to process my guess instantly without requiring a mouse click.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - One example of an incorrect AI suggestion occurred when I asked how to fix the lag in my "Attempts Left" counter and developer debug info. First, the AI model suggested moving those UI elements to the very bottom of the script so they would render after the logic updates. 
  -  I verified this solution by running the app and realizing the layout no longer felt intuitive. While this technically fixed the data lag, it broke the visual layout of the app, moving critical information to a place where the dev wouldn't easily see it unless scrolling down, which is not user friendly. I asked it again if there is any other solution, it said "you can just note it as a bug — the debug panel shows stale (1-turn-delayed) state because it renders before the submit logic runs"
  - Of course, I wasn't happy with its answer because I felt like it should have a better solution. So, I consulted a different model, `Opus 4.6`, which suggested using `st.empty()` placeholders instead. This allowed me to keep the counters and debug info at the top of the page while ensuring they always displayed the most recent data. This second approach fixed the logic error without forcing me to compromise on the interface design.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I considered a bug fixed when the app finally behaved the way a player would expect. The screen had to update immediately without any lag or "stale" numbers showing up. It wasn't enough for the code to just stop crashing. I had to make sure that the numbers I saw in the game and the Developer Debug Info actually matched what was happening behind the scenes in the code.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - I ran a manual test specifically to check if the form was responding to the keyboard `Enter` instead of just mouse clicks.
    - The Test: I typed a guess into the input field and, instead of clicking the `Submit` button with my mouse, I hit the `Enter` key on my keyboard. I did this for several rounds to see if the game would consistently process the guess.
    - The Result: This test confirmed that the `Enter` key was finally mapped to the submission logic. The counter updated the exact moment I hit the key, proving that the form fix worked and that the game could now be played entirely using the keyboard.

- Did AI help you design or understand any tests? How?
  - Yes, the AI helped by explaining that Streamlit runs like a giant loop from top to bottom. I didn't realize that the order of my code was the reason my counters were always one turn behind. The AI suggested that I use the `Developer Debug` section to double-check the actual values in the system against what was being printed on the screen. This made it much easier to see exactly where the lag was happening so I could fix it.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - In the original app, the code to generate the secret number was just a regular line of Python code: `secret = random.randint(1, 100)`. Because of how Streamlit works, every time I clicked a button or typed a guess, the entire script ran again from the very first line. This meant that every single interaction triggered a brand-new random number, making it impossible to actually win since the target was constantly moving.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Imagine Streamlit as a whiteboard that gets fully erased and redrawn every time you click a button. Normally, all your variables disappear with each erase. But `st.session_state` is like a sticky note on the side of the whiteboard, it survives the erase. So if you want something to persist between clicks, like your secret number or score, you have to store it there.
- What change did you make that finally gave the game a stable secret number?
  - Visually, the secret number in the background didn't actually change, but its data type did. Every even-numbered attempt, the code converted the secret number from an integer to a string.  So, I deleted 
  ```python
    if st.session_state.attempts % 2 == 0:
      secret = str(st.session_state.secret)
  ``` 
  Since Python handles integers and strings differently, the comparison logic broke. This made the hints like "Go LOWER!" or "Go HIGHER!" appear at the wrong times, making it seem to the player like the target number had moved when it was really just a math error.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - I want to carry forward the habit of treating AI suggestions as drafts rather than final answers. If a solution feels like a workaround that compromises my design, like moving UI elements to the bottom just to fix a data lag, I will have to keep pushing for a more elegant architectural fix. Interrogating the AI until it provides a professional solution ensures I'm building high-quality systems rather than just "patching" bugs.
- What is one thing you would do differently next time you work with AI on a coding task?
  - Next time, instead of just sticking to one chat thread, I would use comparative prompting earlier. Different models have different "opinions" on best practices. Switching from a model that gave up to one that suggested st.empty() proved that AI is not a single source of truth. It’s a group of consultants, and sometimes you need a second opinion to find the most elegant logic.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - This project made me realize that AI-generated code is just a confident first draft. It might look complete and run without errors, but it can hide subtle logical flaws that only surface during actual use. I’ve learned to treat AI output as a starting point that still requires a human QA lead, especially since the AI that wrote the code isn't there to witness its logic fail in a real-world scenario.

  ## Challenge 5: AI Model Comparison
  - Take one of the logic bugs you found in Phase 1 and ask for a fix from two different models (e.g., Copilot Chat vs. ChatGPT or Gemini).
    - Claude Sonnet 4.6: Suggested moving the code blocks to the bottom of the script. It's still functional but broke the UI layout.
    - Claude Opus 4.6: Suggested using `st.empty()` placeholders. It fixed the bug while keeping the UI clean.
  - In a short section at the bottom of your reflection.md, compare the results. Which model gave a more readable fix? Which one explained the "why" more clearly?
    - Readability: Claude Opus 4.6 was superior because it used `st.empty()` placeholders to fix the data lag without messing up the UI. Claude Sonnet 4.6 suggested moving the code to the bottom, which technically worked but forced the user to scroll down to see their stats.
    - Clarity: Claude Opus 4.6 explained it best by describing the Streamlit `top-to-bottom` execution loop. It clarified that elements at the top render before the logic at the bottom runs, causing the `stale` data lag. Claude Sonnet 4.6 just treated it as a placement issue rather than explaining the actual rendering logic.
