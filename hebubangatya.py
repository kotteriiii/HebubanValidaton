import random
import argparse
import matplotlib.pyplot as plt
import numpy as np


class GatyaManager:
    nomalNum = 0
    nomalFreeQuartz = 0
    nomalList = []

    stepupNum = 0
    stepupFreeQuartz = 0
    stepupPaidQuartz = 0
    stepList = []

    def nomal(self):
        sum = 0
        # 通常ガチャ
        for i in range(20):
            self.nomalFreeQuartz += 3000
            sum += 3000
            if(random.random() < 0.0725187):
                self.nomalNum += 1
                self.nomalList.append(sum)
                return
                
        # 交換
        self.nomalNum += 1
        self.nomalList.append(sum)
        return

    def step(self):
        sum = 0
        # ステップアップガチャ
        for i in range(2):
            # step1
            self.stepupPaidQuartz += 100
            sum += 100
            if(random.random() < 0.0075):
                self.stepupNum += 1
                self.stepList.append(sum)
                return

            # step2
            self.stepupPaidQuartz += 1500
            sum += 1500
            if(random.random() < 0.0725187):
                self.stepupNum += 1
                self.stepList.append(sum)
                return
            
            # step3
            self.stepupPaidQuartz += 2000
            sum += 2000
            if(random.random() < 0.0725187):
                self.stepupNum += 1
                self.stepList.append(sum)
                return
            
            # step4
            self.stepupPaidQuartz += 3000
            sum += 2000
            if(random.random() < 0.1122345):
                self.stepupNum += 1
                self.stepList.append(sum)
                return
            
        # 通常ガチャ
        for i in range(20):
            self.stepupFreeQuartz += 3000
            sum += 3000
            if(random.random() < 0.0725187):
                self.stepupNum += 1
                self.stepList.append(sum)
                return
                
        # 交換
        self.stepupNum += 1
        self.stepList.append(sum)
        return

    def main(self, trials):
        self.nomalNum = 0
        self.nomalFreeQuartz = 0

        self.stepupNum = 0
        self.stepupFreeQuartz = 0
        self.stepupPaidQuartz = 0

        for i in range(trials):
            self.nomal()
            self.step()

        nomalFreeAverage = int(self.nomalFreeQuartz/self.nomalNum)

        stepupFreeAverage = int(self.stepupFreeQuartz/self.stepupNum)
        stepupPaidAverage = int(self.stepupPaidQuartz/self.stepupNum)
        sumQuartz = stepupFreeAverage + stepupPaidAverage

        freeDiff = nomalFreeAverage - stepupFreeAverage
        freeDiv = float(freeDiff/stepupPaidAverage)

        
        print(f"{trials}回試行した結果、ピックアップ対象のあるスタイルを1体入手するのにかかる平均クォーツは")
        print(f"通常ガチャのみ：クォーツ{nomalFreeAverage}")
        print(f"ステップアップガチャ→通常ガチャ：合計クォーツ{sumQuartz}、無償クォーツ{stepupFreeAverage}、有償クォーツ{stepupPaidAverage}")    
        print(f"無償クォーツに対する有償クォーツの価値：{freeDiv:.2f}")

        self.histogram(self.nomalList, "nomal", "red")
        self.histogram(self.stepList, "stepup", "blue")
        plt.show()

        self.cumulativeHistogram(self.nomalList, "nomal", "red")
        self.cumulativeHistogram(self.stepList, "stepup", "blue")
        plt.show()

    def histogram(self, list, label, color):
        # ヒストグラムを作成
        plt.hist(list, bins=50, alpha=0.7, color=color, edgecolor='black', label = label)

        # タイトルとラベルを追加
        plt.title("histogram")
        plt.xlabel('Quartz')
        plt.ylabel('Frequency')

        # 中央値を計算して表示
        median = int(np.median(list))
        plt.axvline(median, color=color, linestyle='dashed', linewidth=1)
        plt.text(median, max(np.histogram(list, bins=50)[0])/2, f'Median: {median}', color=color)

        # 凡例を表示
        plt.legend()

    def cumulativeHistogram(self, list, label, color):

        # 累積度数のヒストグラムを作成
        plt.hist(list, bins=50, alpha=0.5, color=color, edgecolor='black', cumulative=True, label=label)

        # タイトルとラベルを追加
        plt.title("cumulative histogram")
        plt.xlabel('Quartz')
        plt.ylabel('Frequency')

        # 凡例を表示
        plt.legend()
    

# コマンドライン引数の設定
parser = argparse.ArgumentParser()
parser.add_argument("--trials", type=int, default=500000)
args = parser.parse_args()

if __name__ == "__main__":
    instance = GatyaManager()
    instance.main(args.trials)
    



