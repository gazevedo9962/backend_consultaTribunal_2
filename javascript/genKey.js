let key, chars = [
  "a","b","c","d","e","f","g","h",
  "i","j","k","l","m","n","o","p",
  "q","r","s","t","u","v","w","x",
  "y","z","0","1","2","3","4","5",
  "6","7","8","9","!","@","#","%",
  "&","*","(", ")" 
  ];
const geNumRand = () => {
  let r = parseFloat(Math.round(Math.random()*10**2));
  while( r < 0 || r > 43) {
    r = geNumRand();
  }
  return r;
}
const catN = (e,a) => {
  var i = 0 ;
  for ( const element of a) {
    if (element === e) {
      return i ;
      break ; 
    } else  {
      i = i+1;
    }
  }

}
const MaiscOrMins = (e) => {
  let r = parseFloat(Math.round(Math.random()*10**1)), string = e;
  
  if ( r > 5) {
    return string.toUpperCase();
  } else {
    return string.toLowerCase();
  }

}
const genKey = (lengthKey) => {

    var ch,string = '';
    for(var i = 0 ; i <= lengthKey; i++) {
        ch = MaiscOrMins(chars[geNumRand()]);
        string = string + ch ;
    }
 
    return string;

}
console.log(genKey(process.argv[2]))

/*
console.log(key);
console.log(catN("c",chars));
*/
/*
const args = process.argv;
for ( var i = 2 ; i < args.lenght; i++) {
  console.log(args[i])
}
*/