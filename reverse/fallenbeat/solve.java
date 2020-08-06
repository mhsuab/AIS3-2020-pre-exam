import java.util.*;
import java.io.FileReader;
import java.io.BufferedReader;

class solve {      
      public static void main(String args[]) {
            try {
                  FileReader fr = new FileReader("./Fallen_Beat/songs/gekkou/hell.txt");
                  BufferedReader br = new BufferedReader(fr);
                  int bpm = Integer.parseInt(br.readLine());
                  ArrayList<Integer> cache = new ArrayList<>();
                  byte[] flag = new byte[] { 89, 74, 75, 43, 126, 69, 120, 109, 68, 109, 
                  109, 97, 73, 110, 45, 113, 102, 64, 121, 47, 
                  111, 119, 111, 71, 114, 125, 68, 105, 127, 124, 
                  94, 103, 46, 107, 97, 104 };
                  while (br.ready()) {
                        String s = br.readLine();
                        if (s.charAt(0) != '*') {
                              int a = Integer.parseInt(s);
                              cache.add(Integer.valueOf(a));
                        }
                  }
                  for (int i = 0; i < cache.size(); i++) {
                        flag[i % flag.length] = (byte)(flag[i % flag.length] ^ ((Integer)cache.get(i)).intValue());
                  }
                  String fff = new String(flag);
                  System.out.println(fff);
            }
            catch (Exception e) {
                  System.out.println(e);
            }
      }
}


