function fillCourselist(){
    fetch('/lab8/api/courses/')
    .then(function(data){
        return data.json();
    })
    .then(function(courses){
        let tbody=document.getElementById('course-list');
        tbody.innerHTML='';
        for (let i=0; i<courses.length;i++){
            tr=document.createElement('tr');

            let tdName=document.createElement('td');
            tdName.innerText=courses[i].name;

            let tdVideos=document.createElement('td');
            tdVideos.innerText=courses[i].videos;

            let tdPrice=document.createElement('td');
            tdPrice.innerText=courses[i].price || 'free';

            let editButton=document.createElement('button');
            editButton.innerText='редактировать';
            editButton.onclick=function(){
                editCourse(i,courses[i]);
            };
            
            let delButton=document.createElement('button');
            delButton.innerText='удалить';
            delButton.onclick=function(){
                deleteCourse(i);
            }

            let tdDate = document.createElement('td');
            tdDate.innerText = courses[i].date_;

            let tdActions=document.createElement('td');
            tdActions.append(editButton);
            tdActions.append(delButton);

            tr.append(tdName);
            tr.append(tdVideos);
            tr.append(tdPrice);
            tr.append(tdActions);
            tr.append(tdDate);

            tbody.append(tr);
        }
    })
}

    function deleteCourse(num){
        if (!confirm ('are you sure?'))
            return;
        fetch(`/lab8/api/courses/${num}`, {method:'delete'})
        .then(function(){
            fillCourselist();
        });
    }

    function showModal(){
        document.querySelector('div.modal').style.display='block';
    }
    
    function hideModal(){
        document.querySelector('div.modal').style.display='none';
    }
    
    function addCourse(){
        document.getElementById('num').value='';
        document.getElementById('name').value='';
        document.getElementById('videos').value='';
        document.getElementById('price').value='';
        showModal();
    }
    function cancel(){
        hideModal();
    }
    function sendCourse(){
        const num=document.getElementById('num').value;
        const course={
            name:document.getElementById('name').value,
            videos:document.getElementById('videos').value,
            price:document.getElementById('price').value
        }
        const url=`/lab8/api/courses/${num}`;
        const method=num ? 'put':'post';
        fetch(url,{
            method:method,
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(course)
        })
        .then(function(){
            fillCourselist();
            hideModal;
        });
    }

    function editCourse(num,course){
        document.getElementById('num').value=num;
        document.getElementById('name').value=course.name;
        document.getElementById('videos').value=course.videos;
        document.getElementById('price').value=course.price;
        showModal();
    }