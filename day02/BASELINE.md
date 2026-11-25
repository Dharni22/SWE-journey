# Baseline test — 25 Nov 2026

## Correct first try
- FizzBuzz, including the order of conditions
- String reverse with [::-1]
- Palindrome check

## Broken, now fixed
- Word count: looped over characters instead of words; confused key with value

## Fragile, now fixed
- Find max: started at 0, so it failed on all-negative lists

## Still to improve
- Don't shadow built-in names like max, list, str
- Choose test cases that would actually catch the bug

## To learn
- What `for x in y` gives for strings, lists, dicts
- Dictionary key vs value
- Edge cases: empty, negative, single item
