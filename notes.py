import json
import datetime


# Функция для сохранения заметок в файл
def save_notes(notes, file_path="notes.json"):
    with open("notes.json", "w", encoding= "utf-8") as file:
        json.dumps(notes, file, ensure_ascii=False)
        

# Функция для чтения заметок из файла
def load_notes(file_path):
    with open("notes.json", "r", encoding= "utf-8") as file:
        notes = json.load(file)
        
    
# Функция для добавления заметки
def add_note(notes, new_note):
    max_id = max(note['id'] for note in notes) if notes else 0
    new_note['id'] = max_id + 1
    notes.append(new_note)
    
# Функция для редактирования заметки
def edit_note(notes, note_id, new_title=None, new_body=None, new_datetime=None):
    for note in notes:
        if note['id'] == note_id:
            if new_title:
                note['title'] = new_title
            if new_body:
                note['body'] = new_body
            if new_datetime:
                note['datetime'] = new_datetime
            break

# Функция для удаления заметки
def delete_note(notes, note_id):
    notes[:] = [note for note in notes if note['id'] !=note_id]

# Главная функция для взаимодействия с пользователем
def main():
    file_path = 'notes.json'
    notes = load_notes(file_path)
    
    while True:
        print('1. Вывести все заметки')
        print('2. Добавить заметку')
        print('3. Редактировать заметку')
        print('4. Удалить заметку')
        print('5. Выйти')
        
        choice = input('Выберите действие: ')
        
        if choice == '1':
            print('Заметки:')
            for note in notes:
                print(f"ID: {note['id']}")
                print(f"Заголовок: {note['title']}")
                print(f"Текст: {note['body']}")
                print()
            
        elif choice == '2':
            title = input('Введите заголовок заметки: ')
            body = input('Введите текст заметки: ')
            new_note = {
                'title': title,
                'body': body,
                'datetime': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            add_note(notes, new_note)
            save_notes(notes, file_path)
            
        elif choice == '3':
            note_id = int(input('Введите ID заметки для редактирования: '))
            new_title = input('Введите новый заголовок или оставьте пустым: ')
            new_body = input('Введите новый текст заметки или оставьте пустым: ')
            edit_note(notes, note_id, new_title, new_body)
            save_notes(notes, file_path)
            
        elif choice == '4':
            note_id = int(input('Введите ID заметки для удаления: '))
            delete_note(notes, note_id)
            save_notes(notes, file_path)
            
        elif choice == '5':
            break
        else:
            print('Неверный выбор. Попробуйте еще раз. ')
         

if __name__ == '__main__':
    main()
