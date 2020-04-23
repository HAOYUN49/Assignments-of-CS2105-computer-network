
for f in PacketCat/*.in; do
  fsp=${f%%.*}.sp
  python3 PacketList.py < $f > $fsp.tmp
  nr=$(wc -l < $fsp.tmp)
  i=$((nr/10))
  i=$((i<10 ? nr/5 : i))
  echo $f: $i/$nr
  awk "NR % $i == 0" $fsp.tmp > $fsp
  rm $fsp.tmp
done
