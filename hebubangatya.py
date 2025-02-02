import random
import argparse

class GatyaManager:
    nomalNum = 0
    nomalFreeQuartz = 0

    stepupNum = 0
    stepupFreeQuartz = 0
    stepupPaidQuartz = 0

    def nomal(self):
        # 通常ガチャ
        for i in range(20):
            self.nomalFreeQuartz += 3000
            if(random.random() < 0.0725187):
                self.nomalNum += 1
                return
                
        # 交換
        self.nomalNum += 1
        return

    def step(self):
        # ステップアップガチャ
        for i in range(2):
            # step1
            self.stepupPaidQuartz += 100
            if(random.random() < 0.0075):
                self.stepupNum += 1
                return

            # step2
            self.stepupPaidQuartz += 1500
            if(random.random() < 0.0725187):
                self.stepupNum += 1
                return
            
            # step3
            self.stepupPaidQuartz += 2000
            if(random.random() < 0.0725187):
                self.stepupNum += 1
                return
            
            # step4
            self.stepupPaidQuartz += 3000
            if(random.random() < 0.1122345):
                self.stepupNum += 1
                return
            
        # 通常ガチャ
        for i in range(20):
            self.stepupFreeQuartz += 3000
            if(random.random() < 0.0725187):
                self.stepupNum += 1
                return
                
        # 交換
        self.stepupNum += 1
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
        print(f"無償クォーツに対する有償クォーツの価値：{freeDiv}")

# コマンドライン引数の設定
parser = argparse.ArgumentParser()
parser.add_argument("--trials", type=int, default=500000)
args = parser.parse_args()

if __name__ == "__main__":
    instance = GatyaManager()
    instance.main(args.trials)
    



