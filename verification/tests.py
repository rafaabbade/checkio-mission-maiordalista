"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1,2,3,4,5]],
            "answer": 5
        },
        {
            "input": [[-1,0,1,2,3,4]],
            "answer": 4
        },
        {
            "input": [[9,8,7,6,5,4]],
            "answer": 9
        }
    ],
    "Extra": [
        {
            "input": [[-1,-1]],
            "answer": -1
        },
    ]
}
