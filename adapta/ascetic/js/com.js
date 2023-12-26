
        // Обработчик клика на кнопке "Отправить"
        document.querySelector('button').addEventListener('click', function() {
            // Получаем значение поля ввода комментария
            var newComment = document.querySelector('#newComment').value;

            // Создаем новый элемент комментария
            var comment = document.createElement('div');
            comment.classList.add('comment');

            // Создаем элемент аватара пользователя
            var avatar = document.createElement('img');
            avatar.src = 'img/childrenn.jpg'; // путь к файлу относительно корневой папки проекта
            avatar.alt = 'фото пользователя';
            avatar.classList.add('avatar');
            avatar.width = 120;
            avatar.height = 120;
            comment.appendChild(avatar);

            // Создаем блок с контентом комментария
            var commentContent = document.createElement('div');
            commentContent.classList.add('comment-content');

            // Создаем блок с информацией о пользователе
            var userInfo = document.createElement('div');
            userInfo.classList.add('user-info');

            // Добавляем имя пользователя
            var userName = document.createElement('h3');
            userName.textContent = 'Имя пользователя';
            userInfo.appendChild(userName);

            // Добавляем дату комментария
            var commentDate = document.createElement('span');
            commentDate.textContent = new Date().toLocaleString();
            userInfo.appendChild(commentDate);

            commentContent.appendChild(userInfo);

            // Добавляем текст комментария
            var commentText = document.createElement('p');
            commentText.classList.add('comment-text');
            commentText.textContent = newComment;
            commentContent.appendChild(commentText);

            comment.appendChild(commentContent);

            // Добавляем новый комментарий на страницу
            var commentsSection = document.querySelector('h2').nextElementSibling;
            commentsSection.insertBefore(comment, commentsSection.firstChild);

            // Очищаем поле ввода комментария
            document.querySelector('#newComment').value = '';
        });