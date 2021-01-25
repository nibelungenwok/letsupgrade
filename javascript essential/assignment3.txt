<!--Q1-->
function display(lib){
  msg = "";
  for(i = 0; i < lib.length; i++){
    if(lib[i].readingStatus === true){
      msg += "Already read ";
      msg += lib[i].author + " by " + lib[i].title
                    
      }else{
        msg += "You still need to read ";
        msg += lib[i].title + " by " + lib[i].author ;
      }
      msg += '\n'
  }
            return msg;
}
var library = [
  {
    author: 'Bill Gates',
    title: 'The Road Ahead',
    readingStatus: true
  },
  {
    author: 'Steve Jobs',
    title: 'Walter Isaacson',
    readingStatus: true
  },
  {
    author: 'Suzanne Collins',
    title: 'Mockingjay: The Final Book of The Hunger Games',
    readingStatus: false
  }
];

console.log(display(library));

<!--Q2 -->
<html>
    <head>

    </head>
    <body>
        <h1>test</h1>
        <input id='driver_age' placeholder='input your age' >
        <button onclick=validate_age()>test</button>
        <script>
            
            function validate_age(){
                driver_age = document.getElementById('driver_age').value;
                if(driver_age < 18){
                    alert("Not legal age to drive");
                }else{
                    alert("Drive safe");
                }
            }
    </script>
    </body>

</html>
