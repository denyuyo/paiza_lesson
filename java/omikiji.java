// おみくじを作る
public class Main {
	public static void main(String[] args) {
		int omikuji = (int)(Math.random() * 100 + 1);  // randomメソッドについては次のチャプターで説明します
		if (omikuji >= 30) {
			System.out.println("omikujiの中身は" + omikuji + "なので大吉");
		} else {
			System.out.println("omikujiの中身は" + omikuji + "なので大凶");
		}
	}
}

// スライム賽子

// スライムと戦っている。
// 1から10のサイコロをふって、
// 6未満：サイコロの目だけダメージを与えたと表示。
// 6以上：クリティカルヒットとして、100のダメージを与えたと表示。
// さらに、1から2のサイコロをふって、
// 1：追加攻撃として、10のダメージを与えたと表示。
// 2：追加攻撃に失敗したと表示。
public class Main {
	public static void main(String[] args) {
		int hit = (int)(Math.random() * 10 + 1);
		if (hit < 6) {
			System.out.println("スライムに" + hit + "のダメージを与えた");
		} else {
			System.out.println("クリティカルヒット!スライムに、100のダメージを与えた!!");
		}

		int add = (int)(Math.random() * 1 + 1); 
		if (add == 1) { 
			System.out.println("追加攻撃!スライムに、10のダメージを与えた!!!");
		} else {
			System.out.println("追加攻撃に失敗!");
		}
	}
}

// 西暦年から昭和年を求める
public class Main {
	public static void main(String[] args) {
		int seireki = (int)(Math.random() * 63 + 1926);
		System.out.print("西暦" + seireki + "年は");

		// 昭和年を計算
		int showa = seireki - 1925;
		System.out.println("昭和" + showa + "年です。");
	}
}

// 順位に合わせてメッセージを表示する

public class Main {
    public static void main(String[] args) {
        double rand = (Math.random() * 10) + 1;
        int number = (int) rand;
        System.out.println("あなたの順位は" + number + "位です");

        if (number > 1 && number <= 5) {
            System.out.println("あと少し");
        }

    }
}

// 不快指数
public class Main {
    public static void main(String[] args) {
        double rand = (Math.random() * 71) + 30;
        int discomfort = (int) rand;
        System.out.println("不快指数は" + discomfort + "です。");

        if (discomfort <= 55 || discomfort >= 70) {
            System.out.println("不快です");
        }
    }
}

// 順位に合わせてメッセージを表示する

public class Main {
    public static void main(String[] args) {
        double rand = (Math.random() * 10) + 1;
        int number = (int) rand;
        System.out.println("あなたの順位は" + number + "位です");

        boolean flag = number <= 3;
        if (flag) {
            System.out.println("入賞おめでとう");   //条件が成立したときの処理
        }
    }
}