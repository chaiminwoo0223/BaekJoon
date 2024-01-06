package Bronze1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B9093 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 버퍼리더
		int t = Integer.parseInt(br.readLine());                                  // 형변환

		for (int i = 0; i < t; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());              // 토큰 입력

			while (st.hasMoreTokens()) {
				String syntax = st.nextToken();                                   // 토큰 추출
                String reversed = new StringBuilder(syntax).reverse().toString(); // 역순으로 정
                System.out.print(reversed + " ");
            }
			System.out.println();
		}
	}
}