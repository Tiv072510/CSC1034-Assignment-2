class Question:
    def __init__(self, text, options, answers, marks_per_answer, topic,
    last_attempt):
        self.text = text
        self.options = options
        self.answers = answers
        self.marks_per_answer = marks_per_answer
        self.topic = topic
        self.last_attempt = last_attempt
    def get_text(self):
        return self.text
    def get_options(self):
        return self.options
    def get_answers(self):
        return self.answers
    def get_marks_per_answer(self):
        return self.marks_per_answer
    def get_topic(self):
        return self.topic
    def get_last_attempt(self):
        return self.last_attempt
    def __str__(self):
        pass
    def __repr__(self):
        pass
    def __eq__(self, other):
        pass
    def __hash__(self):
        pass
    def get_total_marks(self):
        pass