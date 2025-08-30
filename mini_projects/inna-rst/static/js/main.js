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

    // Ініціалізація вибору іконок (тільки якщо елементи існують)
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

    // Ініціалізація вибору кольору (тільки якщо елементи існують)
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

    // Функція для модального вікна видалення
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

    // Обробники кнопок видалення
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function () {
            const id = this.getAttribute('data-id');
            showDeleteModal(id);
        });
    });

    // Функція для модального вікна видалення
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

    // Обробники кнопок видалення
    const deleteNoteButtons = document.querySelectorAll('.delete-note-btn');
    deleteNoteButtons.forEach(button => {
        button.addEventListener('click', function () {
            const id = this.getAttribute('data-id');
            showDeleteModalNote(id);
        });
    });

});

function initColorSelection() {
    const enableColorCheck = document.querySelector('#enableColorCheck'); // используйте правильный селектор
    const colorSelection = document.querySelector('#colorSelection'); // используйте правильный селектор

    if (!enableColorCheck || !colorSelection) {
        // Ця сторінка не містить елементів вибору кольору
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


    toggleColorSelection();
    enableColorCheck.addEventListener('change', toggleColorSelection);
}

const categoryOptions = document.querySelectorAll('.category-option');
const selectedDisplay = document.getElementById('selectedCategoryDisplay');
const hiddenSelectBlock = document.getElementById('categorySelect');
const dropdownButton = document.getElementById('categoryDropdown');


if (!categoryOptions.length || !selectedDisplay || !hiddenSelectBlock || !dropdownButton) {
    console.log('Required elements for category selection not found');
} else {
    // Функція оновлення відображення
    function updateCategoryDisplay(value, name, icon, color) {
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
    }

    categoryOptions.forEach(option => {
        option.addEventListener('click', function (e) {
            e.preventDefault();
            const value = this.getAttribute('data-value');
            const name = this.getAttribute('data-name');
            const icon = this.getAttribute('data-icon');
            const color = this.getAttribute('data-color');

            hiddenSelectBlock.value = value;
            updateCategoryDisplay(value, name, icon, color);

            const dropdown = bootstrap.Dropdown.getInstance(dropdownButton);
            dropdown && dropdown.hide();
        });
    });

    document.addEventListener('DOMContentLoaded', function () {
        const currentValue = hiddenSelectBlock.value;
        if (currentValue) {
            const activeOption = Array.from(categoryOptions).find(option =>
                option.getAttribute('data-value') === currentValue
            );
            if (activeOption) {
                updateCategoryDisplay(
                    currentValue,
                    activeOption.getAttribute('data-name'),
                    activeOption.getAttribute('data-icon'),
                    activeOption.getAttribute('data-color')
                );
                categoryOptions.forEach(opt => opt.classList.remove('active'));
                activeOption.classList.add('active');
            }
        }
    });
}