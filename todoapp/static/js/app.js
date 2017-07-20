 setTimeout(function(){
                $("#loading").hide()
//                debugger;
                  $.ajax({url: "http://localhost:8000/todo/todoLists/", success: function(result){
                  console.log("result is "+result)
//                  debugger;
                    var markup="<li><label>${name}</label><input type='text'><button  id='${id}' class='dropbtn'>show items</button><button  id='${id}' class='editList'>edit List</button><button  id='${id}' class='deleteList'>delete List</button></li>"
                        $.template( "movieTemplate", markup );
                        $.tmpl( "movieTemplate", result ).appendTo( "#123" );
				}});
}, 2000);
function getCookies(sName){
            var aCookie = document.cookie.split("; ");
            for (var i=0; i < aCookie.length; i++){
              var aCrumb = aCookie[i].split("=");
              if (sName == aCrumb[0])
                return unescape(aCrumb[1]);
            }
            return null;
          }
$("body").on("click",".add",function(){
    item=new Object();
//    debugger;
    console.log($("#list1").val())
    item["name"]=$("#list1").val()
    item["createdDate"]=$("#createDate").val()
//    item["user"]=2

    console.log(item)
    $.ajax({url: "http://localhost:8000/todo/todoLists/",
            type: 'post',
            headers:{
                "X-CSRFToken":getCookies("csrftoken")
            },
            data: item,
            dataType: 'json',
            success: function (data) {
//                debugger;
                x=("<label>"+$("#list1").val()+"</label><input type='text'>")
                var markup="<li>"+x+"<button  id='${id}' class='dropbtn'>show items</button><button  id='${id}' class='editList'>edit List</button><button  id='${id}' class='deleteList'>delete List</button></li>"
                $.template( "movieTemplate", markup );
                $.tmpl( "movieTemplate", data ).appendTo( "#123" );
                $("#list1").val("")
            }
        });
})
$("body").on("click",".editList",function(){
    editTask1(this)
})

// Edit an existing task
var editTask1 = function(but) {
    id=$(but).attr("id")
  var listItem = but.parentNode;
//  debugger;
  var editInput = listItem.querySelector("input[type=text]")
  var label1 = listItem.querySelector("label");
  var label2=listItem.querySelector("p");
  var containsClass = listItem.classList.contains("editMode");
    //if the class of the parent is .editMode
  if(containsClass) {
      //switch from .editMode
      //Make label text become the input's value
    item=new Object()
        item["name"]=editInput.value;
        $.ajax({url: "http://localhost:8000/todo/todoList/"+id+"/",
            headers:{
                "X-CSRFToken":getCookies("csrftoken")
            },
            type: 'put',
            data:item,
            dataType:'json',
            success: function (data) {
//                debugger;
                label1.innerText = editInput.value;
            }
        });
  } else {
      //Switch to .editMode
      //input value becomes the label's text
    editInput.value = label1.innerText;
  }

    // Toggle .editMode on the parent
  listItem.classList.toggle("editMode");

}
$("body").on("click",".dropbtn",function(){
    $(this).parent().parent().parent().parent().attr("id",$(this).attr("id"))
    $("#completed-tasks").empty()
    $("#incomplete-tasks").empty()
//    debugger;
    num=$(this).attr("id")
    console.log("id is "+num)
    $.ajax({url: "http://localhost:8000/todoListItem/"+num, success: function(result){
//                  debugger;
                  for(i=0;i<result.length;i++){
                    if(result[i].completed){
                    var markup='<li id=${id}><input type="checkbox" class="check" checked><label>${description}</label><input type="text"><button class="edit">Edit</button><button class="delete">Delete</button><br><label>Due_by</label><p>${due_by}</p></li>'
                    $.template( "movieTemplate", markup );
                    $("#completed-tasks").append($.tmpl("movieTemplate",result[i]))
                    }
                    else{
                    var markup='<li id=${id}><input type="checkbox" class="check"><label>${description}</label><input type="text"><button class="edit">Edit</button><button class="delete">Delete</button><br><label>Due_by</label><p>${due_by}</p><br><input type="date"></li>'
                    $.template( "movieTemplate", markup );
                    $("#incomplete-tasks").append($.tmpl("movieTemplate",result[i]))
                  }
                  }
				}});
    document.getElementById("myDropdown").classList.toggle("show");
})
$("body").on("click","#sidd",function(){
    addTask(this);
})
// Add a new task
var addTask = function(but) {
  id2=$(but).parent().parent().parent().attr("id")
//  debugger;
  item=new Object();
  item["description"]=$("#new-task").val()
  item["due_by"]=$(".myDate").val()
  item["completed"]="false"
  item["list"]=1
  $.ajax({url: "http://localhost:8000/todo/todoList/"+id2,
            headers:{
                "X-CSRFToken":getCookies("csrftoken")
            },
            type: 'post',
            data: item,
            dataType: 'json',
            success: function (data) {
                debugger;
                x=$('<li><input type="checkbox" class="check"><label>'+$("#new-task").val()+'</label><input type="text"><button class="edit">Edit</button><button class="delete">Delete</button><br><label>Due_by</label><p>'+$(".myDate").val()+'</p><br><input type="date"></li>')
                $("#incomplete-tasks").append(x)
                $('#new-task').val("");
                $(".myDate").val("");
            }
        });
}
$("body").on("click",".edit",function(){
    editTask(this)
})
// Edit an existing task
var editTask = function(but) {
    id=$(but).parent().attr("id")
  var listItem = but.parentNode;
//  debugger;
  var editInput = listItem.querySelector("input[type=text]")
  var label1 = listItem.querySelector("label");
  var label2=listItem.querySelector("p");
  var editDate=listItem.querySelector("input[type=date]")
  var containsClass = listItem.classList.contains("editMode");
  var comp=listItem.querySelector("input[type=checkbox]")
    //if the class of the parent is .editMode
  if(containsClass) {
      //switch from .editMode
      //Make label text become the input's value
    item=new Object()
        item["completed"]="false"
        if(comp.checked){
            item["completed"]="true"
        }
        item["description"]=editInput.value;
        item["due_by"]=editDate.value;
        item['list']=Number($(but).parent().parent().parent().parent().attr("id"))
        $.ajax({url: "http://localhost:8000/todo/todoList/"+id+"/",
            headers:{
                "X-CSRFToken":getCookies("csrftoken")
            },
            type: 'put',
            data:item,
            dataType:'json',
            success: function (data) {
//                debugger;
                label1.innerText = editInput.value;
                label2.innerText=editDate.value;
            }
        });
  } else {
      //Switch to .editMode
      //input value becomes the label's text
    editInput.value = label1.innerText;
    editDate.value=label2.innerText;
  }

    // Toggle .editMode on the parent
  listItem.classList.toggle("editMode");

}
$("body").on("click",".deleteList",function(){
    deleteTask1(this)

    $.ajax({url: "http://localhost:8000/todo/todoLists/", success: function(result){
                  console.log(result)
//                  debugger;
                    var markup="<li><label>${name}</label><input type='text'><button  id='${id}' class='dropbtn'>show items</button><button  id='${id}' class='editList'>edit List</button><button  id='${id}' class='deleteList'>delete List</button></li>"
                        $.template( "movieTemplate", markup );
                        $('#123').empty()
                        $.tmpl( "movieTemplate", result ).appendTo( "#123" );
				}});

})
// Delete an existing task
var deleteTask1 = function(but) {
    id=$(but).attr("id")
  $.ajax({url: "http://localhost:8000/todo/todoList/"+id+"/",
            headers:{
                "X-CSRFToken":getCookies("csrftoken")
            },
            type: 'delete',
            success: function (data) {
                debugger;
                var listItem = but.parentNode;
                var ul = listItem.parentNode;
                ul.removeChild(listItem);
            }
        });
}
$("body").on("click",".delete",function(){
    deleteTask(this)


})
// Delete an existing task
var deleteTask = function(but) {
    id=$(but).parent().attr("id")
  $.ajax({url: "http://localhost:8000/todo/todoListtems/"+id+"/",
            type: 'delete',
            headers:{
                "X-CSRFToken":getCookies("csrftoken")
            },
            success: function (data) {
//                debugger;
                var listItem = but.parentNode;
                var ul = listItem.parentNode;
                ul.removeChild(listItem);
            }
        });
}

$("body").on("change",".check",function(){
    var listItem = this.parentNode;
//  debugger;
  var label1 = listItem.querySelector("label");
  var label2=listItem.querySelector("p");

    id=$(this).parent().attr("id")
    if(this.checked){
        item=new Object()
        item["completed"]="true"
        item["description"]=label1.innerText
        item["due_by"]=label2.innerText
        item['list']=Number($(this).parent().parent().parent().parent().attr("id"))
        $.ajax({url: "http://localhost:8000/todoapp/items/"+id+"/",
            headers:{
                "X-CSRFToken":getCookies("csrftoken")
            },
            type: 'put',
            data:item,
            dataType:'json',
            success: function (data) {
                debugger;
                $("#completed-tasks").append(listItem);
            }
        });
    }
    else{
        item=new Object()
        item["completed"]="false"
        item["description"]=label1.innerText
        item["due_by"]=label2.innerText
        item['list']=Number($(this).parent().parent().parent().parent().attr("id"))
        $.ajax({url: "http://localhost:8000/todo/todoListItems/"+id+"/",
            headers:{
                "X-CSRFToken":getCookies("csrftoken")
            },
            type: 'put',
            data:item,
            dataType:'json',
            success: function (data) {
                debugger;
                $("#incomplete-tasks").append(listItem);
            }
        });
    }
})





