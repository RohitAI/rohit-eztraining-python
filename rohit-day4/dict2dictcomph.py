'''dict={1:"ichigo",2:"bakuya",3:"urahara",4:"renji abarai"}
dict1={no:name for (no,name) in dict.items()}
dict1'''

dict={"avatar":88,"panindia":66,"panworld":89,"globetortting":67}
dict1={movie:rating*1.5 for (movie,rating) in dict.items()}
print(dict1)
