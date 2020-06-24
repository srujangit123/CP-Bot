# !bin/bash
problemCode=$1
contest=$CONTEST


echo "You are in $(pwd)"
problemPath="$(pwd)/${contest}/${contest}${problemCode}"
echo $problemPath
cd $problemPath
g++ -std=c++17 sol.cpp -o solution || { echo "Error while running. Check and run"; exit 1; }

ls -l solution

infiles=(`ls input*.txt`)
# echo ${infiles[@]}
for ((i=0; i<${#infiles[@]}; i++)); do
  ./solution < input$i.txt > youroutput$i.txt 
done


echo Comparing solutions
echo $(pwd)
outputFiles=(`ls output*.txt`)
inputFiles=(`ls input*.txt`)
youroutputFiles=(`ls youroutput*.txt`)

echo ${outputFiles[@]} ${youroutputFiles[@]}
numberOfIOs=${#outputFiles[@]}

echo 

for((i=0; i<$numberOfIOs; i++)) do
  echo TestCase $i
  echo ---------------
  echo Input
  cat ${inputFiles[i]} && echo && echo
  echo Expected Output
  cat ${outputFiles[i]} && echo && echo
  echo Your Output
  cat ${youroutputFiles[i]} && echo
  echo ---------------
  echo
done

cd ..