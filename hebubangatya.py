import random

class GatyaManager:
    nomalNum = 0
    nomalFreeQuartz = 0

    stepupNum = 0
    stepupFreeQuartz = 0
    stepupPaidQuartz = 0

    def nomal(self):
        flag = False
        # 通常ガチャ
        if (flag == False):
            for i in range(20):
                self.nomalFreeQuartz += 3000
                if(random.random() < 0.0725187):
                    self.nomalNum += 1
                    flag = True
                    return
                
        # 交換
        if (flag == False):
            self.nomalNum += 1
            flag = True
            return

    def step(self):
        flag = False
        # ステップアップガチャ
        for i in range(2):
            # step1
            self.stepupPaidQuartz += 100
            if(random.random() < 0.0075):
                self.stepupNum += 1
                flag = True
                return

            # step2
            self.stepupPaidQuartz += 1500
            if(random.random() < 0.0725187):
                self.stepupNum += 1
                flag = True
                return
            
            # step3
            self.stepupPaidQuartz += 2000
            if(random.random() < 0.0725187):
                self.stepupNum += 1
                flag = True
                return
            
            # step4
            self.stepupPaidQuartz += 3000
            if(random.random() < 0.1122345):
                self.stepupNum += 1
                flag = True
                return
            
        # 通常ガチャ
        if (flag == False):
            for i in range(20):
                self.stepupFreeQuartz += 3000
                if(random.random() < 0.0725187):
                    self.stepupNum += 1
                    flag = True
                    return
                
        # 交換
        if (flag == False):
            self.stepupNum += 1
            flag = True
            return

    def main(self, num):
        self.nomalNum = 0
        self.nomalFreeQuartz = 0

        self.stepupNum = 0
        self.stepupFreeQuartz = 0
        self.stepupPaidQuartz = 0

        for i in range(num):
            self.nomal()
            self.step()

        nomalFreeAverage = int(self.nomalFreeQuartz/self.nomalNum)

        stepupFreeAverage = int(self.stepupFreeQuartz/self.stepupNum)
        stepupPaidAverage = int(self.stepupPaidQuartz/self.stepupNum)
        sumQuartz = stepupFreeAverage + stepupPaidAverage

        freeDiff = nomalFreeAverage - stepupFreeAverage
        freeDiv = float(freeDiff/stepupPaidAverage)

        
        print("ピックアップ対象のあるスタイルを1体入手するのにかかる平均クォーツは")
        print(f"通常ガチャのみ：クォーツ{nomalFreeAverage}")
        print(f"ステップアップガチャ→通常ガチャ：合計クォーツ{sumQuartz}、無償クォーツ{stepupFreeAverage}、有償クォーツ{stepupPaidAverage}")    
        print(f"無償クォーツに対する有償クォーツの価値：{freeDiv}")

        # print(self.nomalNum)
        # print(self.nomalFreeQuartz)
        # print(self.stepupNum)
        # print(self.stepupFreeQuartz)
        # print(self.stepupPaidQuartz) 

if __name__ == "__main__":
    instance = GatyaManager()
    instance.main(500000)
    



