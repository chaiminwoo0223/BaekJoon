package Silver4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class B18258 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 버퍼리더
		int n = Integer.parseInt(br.readLine());                                  // 형변환
		Deque<Integer> deque = new LinkedList<>();                                // 데크(덱)

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());              // 토큰 입력
			String cmd = st.nextToken();                                          // 토큰 추출
			if (cmd.equals("push")) {
				deque.push(Integer.parseInt(st.nextToken()));
			}
			else if (cmd.equals("pop")) {
				if (deque.isEmpty()) { System.out.println(-1); }
				else { System.out.println(deque.pop()); }
			}
			else if (cmd.equals("size")) {
				System.out.println(deque.size());
			}
			else if (cmd.equals("empty")) {
				System.out.println(deque.isEmpty() ? 1 : 0);
			}
			else if (cmd.equals("front")) {
				if (deque.isEmpty()) { System.out.println(-1); }
				else { System.out.println(deque.getLast()); }
			}
			else if (cmd.equals("back")) {
				if (deque.isEmpty()) { System.out.println(-1); }
				else { System.out.println(deque.getFirst()); }
			}
		}
	}
}