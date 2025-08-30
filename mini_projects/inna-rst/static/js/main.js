document.addEventListener('DOMContentLoaded', function () {
    'use strict';

    // Header Search Toggle
    const searchWrapper = document.querySelector('.header-search-wrapper');
    const body = document.body;
    const searchToggle = document.querySelector('.search-toggle');
    const headerSearch = document.querySelector('.header-search');

    function toggleClass(element, className) {
        if (element.classList.contains(className)) {
            element.classList.remove(className);
        } else {
            element.classList.add(className);
        }
    }

    // Обробник кліка на кнопку пошуку
    if (searchToggle) {
        searchToggle.addEventListener('click', function (e) {
            if (searchWrapper) {
                toggleClass(searchWrapper, 'show');
                toggleClass(searchToggle, 'active');

                // Фокус на полі введення
                const input = searchWrapper.querySelector('input');
                if (input) {
                    input.focus();
                }
            }
            e.preventDefault();
        });
    }

    // Обробник кліка за документом (закриття пошуку при кліку поза ним)
    body.addEventListener('click', function (e) {
        if (searchWrapper && searchWrapper.classList.contains('show')) {
            searchWrapper.classList.remove('show');
            if (searchToggle) {
                searchToggle.classList.remove('active');
            }
            body.classList.remove('is-search-active');
        }
    });

    // Запобігання закриття пошуку при натисканні на сам елемент пошуку
    if (headerSearch) {
        headerSearch.addEventListener('click', function (e) {
            e.stopPropagation();
        });
    }

     // Инициализация выбора иконок (только если элементы существуют)
    const iconOptions = document.querySelectorAll('.icon-option');
    const hiddenSelect = document.getElementById('iconSelect');

    if (hiddenSelect && iconOptions.length > 0) {
        function syncSelection() {
            const currentValue = hiddenSelect.value;
            iconOptions.forEach(option => {
                if (option.getAttribute('data-value') === currentValue) {
                    option.classList.add('selected');
                } else {
                    option.classList.remove('selected');
                }
            });
        }

        syncSelection();

        iconOptions.forEach(option => {
            option.addEventListener('click', function () {
                const iconValue = this.getAttribute('data-value');
                hiddenSelect.value = iconValue;
                syncSelection();
            });
        });
    }

    // Инициализация выбора цвета (только если элементы существуют)
    const enableColorCheck = document.querySelector('#enableColorCheck');
    const colorSelection = document.querySelector('#colorSelection');

    if (enableColorCheck && colorSelection) {
        function toggleColorSelection() {
            if (enableColorCheck.checked) {
                colorSelection.style.display = 'block';
                colorSelection.style.opacity = '0';
                setTimeout(() => {
                    colorSelection.style.transition = 'opacity 0.3s ease';
                    colorSelection.style.opacity = '1';
                }, 10);
            } else {
                colorSelection.style.transition = 'opacity 0.3s ease';
                colorSelection.style.opacity = '0';
                setTimeout(() => {
                    colorSelection.style.display = 'none';
                }, 300);
            }
        }

        toggleColorSelection();
        enableColorCheck.addEventListener('change', toggleColorSelection);
    }

    // Функция для модального окна удаления
    function showDeleteModal(categoryId) {
        fetch(`/categories/${categoryId}/details`)
            .then(response => response.json())
            .then(category => {
                document.getElementById('categoryNameToDelete').textContent = `"${category.name}"`;
                document.getElementById('deleteForm').action = `/categories/${categoryId}/delete`;

                const modal = new bootstrap.Modal(document.getElementById('deleteCategoryModal'));
                modal.show();
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Помилка завантаження даних категорії');
            });
    }

    // Обработчики кнопок удаления
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function () {
            const id = this.getAttribute('data-id');
            showDeleteModal(id);
        });
    });

      // Функция для модального окна удаления
    function showDeleteModalNote(noteId) {
        fetch(`/notes/${noteId}/details`)
            .then(response => response.json())
            .then(note => {
                document.getElementById('noteNameToDelete').textContent = `"${note.title}"`;
                document.getElementById('deleteNoteForm').action = `/notes/${noteId}/delete`;

                const modal = new bootstrap.Modal(document.getElementById('deleteNoteModal'));
                modal.show();
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Помилка завантаження даних нотатки');
            });
    }

    // Обработчики кнопок удаления
    const deleteNoteButtons = document.querySelectorAll('.delete-note-btn');
    deleteNoteButtons.forEach(button => {
        button.addEventListener('click', function () {
            const id = this.getAttribute('data-id');
            showDeleteModalNote(id);
        });
    });

    const categoryOptions = document.querySelectorAll('.category-option');
    const selectedDisplay = document.getElementById('selectedCategoryDisplay');
    const hiddenSelectBlock = document.getElementById('categorySelect');
    const dropdownButton = document.getElementById('categoryDropdown');

    if (!categoryOptions.length || !selectedDisplay || !hiddenSelectBlock) {
        return;
    }

    categoryOptions.forEach(option => {
        option.addEventListener('click', function(e) {
            e.preventDefault();

            const value = this.getAttribute('data-value');
            const name = this.getAttribute('data-name');
            const icon = this.getAttribute('data-icon');
            const color = this.getAttribute('data-color');

            // Обновляем скрытое поле
            hiddenSelectBlock.value = value;

            // Обновляем отображение
            let displayHtml = '';
            if (icon) {
                displayHtml += `<i class="bi ${icon} me-2"`;
                if (color) displayHtml += ` style="color: ${color};"`;
                displayHtml += `></i>`;
            } else if (value === '0') {
                displayHtml += '<i class="bi bi-x-circle me-2 text-muted"></i>';
            } else {
                displayHtml += '<i class="bi bi-folder me-2 text-muted"></i>';
            }
            displayHtml += `<span>${name}</span>`;

            selectedDisplay.innerHTML = displayHtml;

            // Закрываем dropdown
            const dropdown = bootstrap.Dropdown.getInstance(dropdownButton);
            if (dropdown) {
                dropdown.hide();
            }
        });
    });
});

function initColorSelection() {
    const enableColorCheck = document.querySelector('#enableColorCheck'); // используйте правильный селектор
    const colorSelection = document.querySelector('#colorSelection'); // используйте правильный селектор

    if (!enableColorCheck || !colorSelection) {
        // Эта страница не содержит элементы выбора цвета
        return;
    }

    function toggleColorSelection() {
        if (enableColorCheck.checked) {
            colorSelection.style.display = 'block';
            colorSelection.style.opacity = '0';
            setTimeout(() => {
                colorSelection.style.transition = 'opacity 0.3s ease';
                colorSelection.style.opacity = '1';
            }, 10);
        } else {
            colorSelection.style.transition = 'opacity 0.3s ease';
            colorSelection.style.opacity = '0';
            setTimeout(() => {
                colorSelection.style.display = 'none';
            }, 300);
        }
    }

    // Проверить состояние при загрузке страницы
    toggleColorSelection();
    // Добавить обработчик события
    enableColorCheck.addEventListener('change', toggleColorSelection);
}

// Запустить инициализацию после загрузки DOM
document.addEventListener('DOMContentLoaded', initColorSelection);