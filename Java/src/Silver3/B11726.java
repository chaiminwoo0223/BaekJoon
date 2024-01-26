package Silver3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B11726 {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] cnt = new int[n + 1];
        cnt[1] = 1;
        if(n > 1) {
        	cnt[2] = 2;
        }
        for (int i = 3; i <= n; i++) {
            cnt[i] = (cnt[i - 1] + cnt[i - 2]) % 10007;
        }
        System.out.println(cnt[n]);
    }
}