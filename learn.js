const members = [
    
    {
        name:"Subhodip Ghosh",
        age:35,
        maritalStatus:true,
        nickName:["Kunal","Subho"]
    },
    {
        name:"Tonmoy Roy",
        age:22,
        maritalStatus:false,
        nickName:["Bradu","Naran"]
    },
    {
        name:"Shubhom Mondal",
        age:23,
        maritalStatus:false,
        nickName:["Betal"]
    },
    {
        name:"Adipto Roy",
        age:22,
        maritalStatus:false,
        nickName:["Ribhu"]
    },
    {
        name:"Diptodip Biswas",
        age:21,
        maritalStatus:false,
        nickName:["Rocket","Lebu"]
    }
        
];

// console.log(members);


let som = {
        name:"Som Mondal",
        age:21,
        maritalStatus:false,
        nickName:["Bittu","Babu"]
    };

members[members.length]=som;

// console.log(members);
/*
members.forEach((x)=>{
    console.log(x.name);
})
*/
/*
members.map((value,index)=>{
    console.log(`index is ${index} and name is ${value.name}`);
    
})
*/

let sum = 0
members.forEach((x)=>{
    sum+=x.age;
})



function search(attr,vlu) {

    //console.log(typeof(members[0][attr]) , typeof(vlu));
    
    //1st
    if( typeof(members[0][attr]) != typeof(vlu) ){
        console.log("Type not match");
        return;
    }
    //2ed
    members.forEach((x)=>{
        if (x[attr] == vlu) {
            console.log("found ",x);
        }
    })
}

function searchModi(attr,vlu) {

    const type = {
        name : "string",
        age : "number",
        maritalStatus : "boolean",
        nickName : "string"
    }
    
    //1st
    console.log("\n",attr,vlu);
    console.log(typeof(vlu))
    
    if( type[attr] != typeof(vlu) ){
        console.log("Type not match");
        return;
    }else{
        console.log("prossed");
        
    }
    //2ed

    
}




searchModi("age",22)
searchModi("age","22")

searchModi("name","Som Mondal")
searchModi("name",true)

searchModi("maritalStatus",true)
searchModi("maritalStatus","true")

searchModi("nickName","dipto")
searchModi("nickName",33)

let arr = ["klfkmk",",vlc,l0","kglkbgfkl"]

let ob = {
    p1 : 'value',
    p2 : 12,
    p3 : true
}

searchModi("nickName",arr)
searchModi("nickName",ob)


/*
console.log(`search("age","22")`);
search("age","22")

console.log(`search("age",22)`);
search("age",22)

console.log(`search("maritalStatus",true)`);
search("maritalStatus",true)

console.log(`search("maritalStatus","false")`);
search("maritalStatus","false")


search("nickName","Rocket")
*/

/*
console.log(`search("name","Som Mondal")`);
search("name","Som Mondal")

console.log(`search("age","22")`);
search("age","22")

console.log(`search("age",22)`);
search("age",22)

console.log(`search("maritalStatus",true)`);
search("maritalStatus",true)

console.log(`search("maritalStatus","false")`);
search("maritalStatus","false")


search("nickName","Rocket")

*/
/*
const prr = (a)=>{
    console.log(a);
    
}

prr("hola")
*/

// console.log(members[members.length-1]);

let a = 10
// console.log(a instanceof Number);

// console.log(Number.isInteger(a));

members.push(som)
// console.log(members);


try {
  let x = Math.round(4.6);
}
catch(err) {
  let text = err.name + " " + err.description;
    console.log(text);
    
}

const apples = {name: 'Apples'};
const bananas = {name: 'Bananas'};
const oranges = {name: 'Oranges'};

// Create a Map
const fruits = new Map();

// Add the Objects to the Map
fruits.set(apples, 500);
fruits.set(bananas, 300);
fruits.set(oranges, 200);

console.log(fruits);
