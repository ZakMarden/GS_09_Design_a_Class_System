class DiaryEntry():
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.contact_name_and_number = {}
        self.words = contents.split()
        self.word_count = len(self.words)
        self.chunk_start_point = 0

    def reading_time(self, wpm):
        # input: reading speed, entry contents
        # output: float representing time to read entry in minutes
        # other: None
        return self.word_count / wpm

    def reading_chunks(self, wpm, minutes):
        # input: reading speed and time
        # output: chunk of entry to be read
        # other: none
        if self.chunk_start_point >= self.word_count:
            self.chunk_start_point = 0
        chunk_size_in_words = wpm * minutes
        chunk_end_point = self.chunk_start_point + chunk_size_in_words
        chunk = " ".join(self.words[self.chunk_start_point:chunk_end_point])
        self.chunk_start_point = chunk_end_point
        return chunk

    def add_contact(self, contact_name, number):
        # input: contact name and number
        # output: none
        # other: update contact list dictionary
        self.contact_name_and_number.update({contact_name: number})
