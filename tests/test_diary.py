from lib.diary import *
from lib.diary_entry import *
from lib.task_entry import *

#DIARY_ENTRY UNIT TESTS
#1 test reading time method
def test_reading_time():
    entry = DiaryEntry("test title", "test contents")
    assert entry.word_count == 2
    assert entry.reading_time(2) == 1

#2 test reading chunks method
def test_reading_chunks():
    entry = DiaryEntry("test title", "test contents")
    assert entry.reading_chunks(1, 1) == "test"
    assert entry.reading_chunks(1, 1) == "contents"
    assert entry.reading_chunks(1, 2) == "test contents"
    assert entry.reading_chunks(1, 1) == "test"
    assert entry.reading_chunks(2, 1) == "contents"
    assert entry.reading_chunks(2, 1) == "test contents"

#3 test get contact method
def test_get_contact():
    entry = DiaryEntry("test title", "test contents")
    assert entry.contact_name_and_number == {}
    entry.add_contact("test name", "12345")
    assert entry.contact_name_and_number == {"test name": "12345"}

#TASK_ENTRY UNIT TESTS
#1 test task creation
def test_task_creation():
    task = TaskEntry("test task")
    assert task.task == "test task"
    assert task.completed == False

#2 test mark completed method
def test_mark_complete():
    task = TaskEntry("test task")
    task.mark_complete()
    assert task.completed == True

#DIARY UNIT TESTS

#DIARY INTEGRATION TESTS
#1 test add entry
def test_int_add_entry():
    diary = Diary()
    entry = DiaryEntry("test title", "test contents")
    diary.add_entry(entry)
    assert diary.diary_entry_list == [entry]

#2 test add task
def test_int_add_task():
    diary = Diary()
    task = TaskEntry("test task")
    diary.add_task(task)
    assert diary.task_list == [task]

#3 get numbered list of entries
def test_int_get_list_entries():
    diary = Diary()
    entry = DiaryEntry("test title", "test contents")
    entry2 = DiaryEntry("test title2", "test contents2")
    diary.add_entry(entry)
    diary.add_entry(entry2)
    assert diary.get_list_of_diary_entries() == "1. test title\n2. test title2"

#4 get diary entry from index number
def test_int_get_diary_entry_content():
    diary = Diary()
    entry = DiaryEntry("test title", "test contents")
    entry2 = DiaryEntry("test title2", "test contents2")
    diary.add_entry(entry)
    diary.add_entry(entry2)
    assert diary.get_diary_entry_from_title(2) == "test contents2"

#5 get list of tasks, full details
def test_int_get_task_report():
    diary = Diary()
    task1 = TaskEntry("test task1")
    task2 = TaskEntry("test task2")
    task3 = TaskEntry("test task3")
    diary.add_task(task1)
    diary.add_task(task2)
    diary.add_task(task3)
    assert diary.get_task_report() == '0% of tasks completed\nIncomplete Task(s):\ntest task1\ntest task2\ntest task3\nCompleted Task(s):\n'
    task1.mark_complete()
    assert diary.get_task_report() == '33% of tasks completed\nIncomplete Task(s):\ntest task2\ntest task3\nCompleted Task(s):\ntest task1'

#6 get list of contacts and numbers
def test_int_get_contacts_1_entry_has_1_contact():
    diary = Diary()
    entry = DiaryEntry("test title", "test contents")
    entry2 = DiaryEntry("test title2", "test contents2")
    diary.add_entry(entry)
    diary.add_entry(entry2)
    entry.add_contact("Test Contact", "12345")
    assert diary.get_list_of_phone_numbers() == "Test Contact: 12345"

def test_int_get_contacts_2_entries_have_1_contact_each():
    diary = Diary()
    entry = DiaryEntry("test title", "test contents")
    entry2 = DiaryEntry("test title2", "test contents2")
    diary.add_entry(entry)
    diary.add_entry(entry2)
    entry.add_contact("Test Contact", "12345")
    entry2.add_contact("TestContact2", "67890")
    assert diary.get_list_of_phone_numbers() == "Test Contact: 12345\nTestContact2: 67890"

def test_int_get_contacts_1_entry_has_2_contacts():
    diary = Diary()
    entry = DiaryEntry("test title", "test contents")
    entry2 = DiaryEntry("test title2", "test contents2")
    diary.add_entry(entry)
    diary.add_entry(entry2)
    entry.add_contact("Test Contact", "12345")
    entry.add_contact("TestContact2", "67890")
    assert diary.get_list_of_phone_numbers() == "Test Contact: 12345\nTestContact2: 67890"

def test_int_get_contacts_2_entries_have_2_contacts_each():
    diary = Diary()
    entry = DiaryEntry("test title", "test contents")
    entry2 = DiaryEntry("test title2", "test contents2")
    diary.add_entry(entry)
    diary.add_entry(entry2)
    entry.add_contact("Test Contact", "12345")
    entry.add_contact("TestContact2", "67890")
    entry2.add_contact("Test Contact", "1234567")
    entry2.add_contact("TestContact3", "54321")
    assert diary.get_list_of_phone_numbers() == "Test Contact: 1234567\nTestContact2: 67890\nTestContact3: 54321"

#7 get best entry for given reading time
def test_int_find_best_entry():
    diary = Diary()
    entry = DiaryEntry("test title", "1 2")
    entry2 = DiaryEntry("test title2", "1 2 3 4")
    entry3 = DiaryEntry("test title2", "1 2 3 4 5 6")
    diary.add_entry(entry)
    diary.add_entry(entry2)
    diary.add_entry(entry3)
    assert diary.find_best_entry_for_reading_time(5, 1) == entry2

#8 read entry in chunks
def test_int_read_entry_in_chunks():
    diary = Diary()
    entry = DiaryEntry("test title", "1 2")
    entry2 = DiaryEntry("test title2", "1 2 3 4")
    entry3 = DiaryEntry("test title2", "1 2 3 4 5 6")
    diary.add_entry(entry)
    diary.add_entry(entry2)
    diary.add_entry(entry3)
    assert diary.read_entry_in_chunks(3, 2, 1) == "1 2"
    assert diary.read_entry_in_chunks(3, 2, 1) == "3 4"
    assert diary.read_entry_in_chunks(3, 2, 1) == "5 6"
    assert diary.read_entry_in_chunks(3, 5, 1) == "1 2 3 4 5"
    assert diary.read_entry_in_chunks(3, 5, 1) == "6"