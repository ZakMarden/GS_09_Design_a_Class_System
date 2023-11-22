class Diary():
    def __init__(self):
        self.diary_entry_list = []
        self.task_list = []
        self.contact_dict = {}
        pass

    def add_entry(self, entry):
        # input: instance of DiaryEntry class
        # output: none
        # other: .append to list of diary entries
        self.diary_entry_list.append(entry)
        pass

    def add_task(self, task):
        # input: instance of TaskEntry class
        # output: none
        # other: .append to list of tasks
        self.task_list.append(task)
        pass

    def get_list_of_diary_entries(self):
        # input: self.diary_entry_list
        # output: numbered list of diary entry titles
        # other: none
        if self.diary_entry_list == []:
            return "No entries"
        else:
            return "\n".join([f"{str(i + 1)}. {self.diary_entry_list[i].title}" for i in range(len(self.diary_entry_list))])

    def get_diary_entry_from_title(self, entry_index):
        # input: index of diary entry from get_list_of_diary_entries()
        # output: content of diary entry with that title
        # other: should alert user in some way if the title they are looking for is not associated with an entry
        if 0 < entry_index <= len(self.diary_entry_list):
            return self.diary_entry_list[entry_index - 1].contents
        else:
            return "No entry for that index"

    def get_task_report(self):
        # input: self.task_list
        # output: list of incomplete tasks, list of completed tasks, and percentage completion
        # other: should alert user if there are no tasks
        if self.task_list == []:
            return "No tasks"
        else:
            completed_tasks = [task.task for task in self.task_list if task.completed == True]
            incomplete_tasks = [task.task for task in self.task_list if task.completed == False]
            percent_complete = int((len(completed_tasks) / (len(completed_tasks) + len(incomplete_tasks))) * 100)
            incomplete_list = 'Incomplete Task(s):\n' + "\n".join(incomplete_tasks)
            complete_list = 'Completed Task(s):\n' + "\n".join(completed_tasks)
            return f'{percent_complete}% of tasks completed\n{incomplete_list}\n{complete_list}'

    def get_list_of_phone_numbers(self):
        # input: self.diary_entry_list
        # output: list of all contacts and their phone numbers
        # other: should alert user if no contacts
        if self.diary_entry_list == []:
            return "No entries"
        else:
            for entry in self.diary_entry_list:
                if entry.contact_name_and_number == {}:
                    continue
                else:
                    self.contact_dict.update(entry.contact_name_and_number)
            return "\n".join([f"{contact[0]}: {contact[1]}" for contact in self.contact_dict.items()])

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # input: self.diary_entry_list, reading speed and time available
        # output: most appropriate entry for them to read
        # other: should alert user if there are no appropriate entries
        words_can_read = wpm * minutes
        entries_not_over = [x for x in self.diary_entry_list if x.word_count <= words_can_read]
        if entries_not_over == []:
            return "No suitable entries"
        else:
            return max(entries_not_over, key = lambda x: x.word_count)

    def read_entry_in_chunks(self, entry_index, wpm, minutes):
        # input: number of diary entry, reading speed, time available
        # output: contents of entry in chunks of selected size
        # other: none
        if 0 < entry_index <= len(self.diary_entry_list):
            return self.diary_entry_list[entry_index - 1].reading_chunks(wpm, minutes)
        else:
            return "No entry for that index"