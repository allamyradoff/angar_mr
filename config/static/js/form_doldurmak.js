console.log("baglandy");

let car_ids = document.getElementById("carid"); 
let car_names = document.getElementById("car_name"); 

let input_for_category_name_show = document.getElementById("catid_show");
let input_for_post_data = document.getElementById("catid");

let input_rating = document.getElementById("rating");

// document.getElementById("{{i.id}}").setAttribute("disabled", "disabled")


function test(id, name) {
    console.log("ID ", id)
    car_names.value = car_names.value + name + "; ";
    car_ids.value = car_ids.value + id + ";";
    document.getElementById(id).setAttribute("disabled", "disabled");
};

function category_set_data(id, name){
    console.log("id : ", id, "name: ", name)
    input_for_category_name_show.value =  name ;
    input_for_post_data.value =  id ;
    document.getElementById("cart_id_name").style.display  = "none";
};

function setStatus(status){
    input_rating.value = status;
};


function deleteProduct(id, name){
    if (prompt(name , "Chyndanam pozjakmy?") !== null){
        // document.getElementById(id).setAttribute("href", "{% url 'delete_zapcas' "+id+" %}");
        const as = "{% url 'delete_zapcas' "+id+" %}"
        console.log(typeof as, as);
    };

    // href="{% url 'delete_zapcas' i.id %}"
};
