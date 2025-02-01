### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    match question:
        case "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
            return "pcap"
        case "Are encoding and encryption the same? - Yes/No":
            return "No"
        case "Is it possible to decrypt a message without a key? - Yes/No":
            return "No"
        case "Is it possible to decode a message without a key? - Yes/No":
            return "Yes"
        case "Is a hashed message supposed to be un-hashed? - Yes/No":
            return "No"
        case "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
            nyu_email = "vl2299@nyu.edu"
            sha256_hash = hashlib.sha256(nyu_email.encode()).hexdigest()
            return ""
        case "Is MD5 a secured hashing algorithm? - Yes/No":
            return "No"
        case "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
            return "5"
        case "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
            return "3"
        case _:
            # Default case if the question doesn't match any case
            return "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
# Complete all the questions.


if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))

#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?": pcap
#"Are encoding and encryption the same? - Yes/No":
#"Is it possible to decrypt a message without a key? - Yes/No":
#"Is it possible to decode a message without a key? - Yes/No":
#"Is a hashed message supposed to be un-hashed? - Yes/No":
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
#"Is MD5 a secured hashing algorithm? - Yes/No":
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
