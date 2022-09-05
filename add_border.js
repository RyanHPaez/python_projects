function solution(picture) {
    let maxlength = 0
    for (let i=0;i<picture.length;i++){
      if(picture[i].length>maxlength){
        maxlength= picture[i].length
      }
    }
    let border = "*".repeat(maxlength+2);
    let resultArr =[border,border]
  for (let i=0;i<picture.length;i++){
      resultArr.splice(i+1,0,"\*"+picture[i]+"\*")
  } return resultArr
  }
  