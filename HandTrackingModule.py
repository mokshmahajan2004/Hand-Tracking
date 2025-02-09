{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ca1fedea-8189-4974-9491-bb74fa45a37e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import mediapipe as mp\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9276f2ca-da36-4639-9ff0-076424d9ea8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# class handDetector:\n",
    "#     def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):\n",
    "#         self.mode = mode\n",
    "#         self.maxHands = maxHands\n",
    "#         self.detectionCon = detectionCon\n",
    "#         self.trackCon = trackCon\n",
    "        \n",
    "#         self.mpHands = mp.solutions.hands\n",
    "#         self.hands = self.mpHands.Hands(\n",
    "#             static_image_mode=self.mode,\n",
    "#             max_num_hands=self.maxHands,\n",
    "#             min_detection_confidence=float(self.detectionCon),\n",
    "#             min_tracking_confidence=float(self.trackCon)\n",
    "#         )\n",
    "#         self.mpDraw = mp.solutions.drawing_utils\n",
    "\n",
    "#     def findHands(self, img, draw=True):\n",
    "#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)\n",
    "#         self.results = self.hands.process(imgRGB)\n",
    "#         if self.results.multi_hand_landmarks:\n",
    "#             for handLms in self.results.multi_hand_landmarks:\n",
    "#                 if draw:\n",
    "#                     self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)\n",
    "#         return img\n",
    "#     def findPosition(self,img,handNo=0,draw=True):\n",
    "#         lmList=[]\n",
    "#         if self.results.multi_hand_landmarks:\n",
    "#             myHand= self.results.multi_hand_landmarks[handNo]\n",
    "#             for id,lm in enumerate(handLms.landmark):\n",
    "#                 #     #print(id,lm)\n",
    "#                     h, w, c =img.shape\n",
    "#                     cx, cy = int(lm.x*w),int(lm.y*h)\n",
    "#                    # print(id,cx,cy)\n",
    "#                     lmList.append([id,cx,cy])\n",
    "#                     if draw:\n",
    "#                       cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)\n",
    "#             return lmList\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ba832af8-af47-4955-b84a-3ba87440e092",
   "metadata": {},
   "outputs": [],
   "source": [
    "# def main():\n",
    "#     pTime=0\n",
    "#     cTime=0\n",
    "#     cap=cv2.VideoCapture(0)\n",
    "#     detector=handDetector(detectionCon=0.5, trackCon=0.5)\n",
    "#     while True:\n",
    "#         sucess,img=cap.read()\n",
    "#         img=detector.findHands(img)\n",
    "#         lmList=detector.findPosition(img)\n",
    "#         if lmList  and len(lmList) != 0:\n",
    "#             print(lmList[4])\n",
    "#         cTime=time.time()\n",
    "#         fps=1/(cTime-pTime)\n",
    "#         pTime=cTime\n",
    "#         cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)\n",
    "#         cv2.imshow(\"Image\",img)\n",
    "#         if cv2.waitKey(1)& 0xFF == ord('q'):\n",
    "#             break\n",
    "\n",
    "#     cap.release()\n",
    "#     cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c1d373ea-d8c4-45d6-acbe-7fb720976fe4",
   "metadata": {},
   "outputs": [],
   "source": [
    "class handDetector:\n",
    "    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):\n",
    "        self.mode = mode\n",
    "        self.maxHands = maxHands\n",
    "        self.detectionCon = detectionCon\n",
    "        self.trackCon = trackCon\n",
    "        \n",
    "        self.mpHands = mp.solutions.hands\n",
    "        self.hands = self.mpHands.Hands(\n",
    "            static_image_mode=self.mode,\n",
    "            max_num_hands=self.maxHands,\n",
    "            min_detection_confidence=float(self.detectionCon),\n",
    "            min_tracking_confidence=float(self.trackCon)\n",
    "        )\n",
    "        self.mpDraw = mp.solutions.drawing_utils\n",
    "\n",
    "    def findHands(self, img, draw=True):\n",
    "        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)\n",
    "        self.results = self.hands.process(imgRGB)\n",
    "        if self.results.multi_hand_landmarks:\n",
    "            for handLms in self.results.multi_hand_landmarks:\n",
    "                if draw:\n",
    "                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)\n",
    "        return img\n",
    "\n",
    "    def findPosition(self, img, handNo=0, draw= True ):\n",
    "        lmList = []\n",
    "        if self.results.multi_hand_landmarks:\n",
    "            myHand = self.results.multi_hand_landmarks[handNo] \n",
    "            for id, lm in enumerate(myHand.landmark):\n",
    "                # print(id,lm)\n",
    "                h, w, c =img.shape\n",
    "                cx, cy = int(lm.x * w),int(lm.y * h)\n",
    "                lmList.append([id, cx, cy])\n",
    "                if draw:\n",
    "                    cv2.circle(img, (cx, cy),15, (255,0,255), cv2.FILLED)      \n",
    "            return lmList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0ab279a6-fb69-4be6-a110-52a39c68c5e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    pTime=0\n",
    "    cTime=0\n",
    "    cap=cv2.VideoCapture(0)\n",
    "    detector=handDetector(detectionCon=0.5, trackCon=0.5)\n",
    "    while True:\n",
    "        sucess, img=cap.read()\n",
    "        img=detector.findHands(img, draw=True)\n",
    "        lmList = detector.findPosition(img, draw=True)\n",
    "        # if len(lmList) != 0:\n",
    "        #     print(lmList[4])\n",
    "        if lmList:  # Check if lmList is not empty\n",
    "            print(lmList[4])\n",
    "        \n",
    "        cTime=time.time()\n",
    "        fps=1/(cTime-pTime)\n",
    "        pTime=cTime\n",
    "        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)\n",
    "        cv2.imshow(\"Image\",img)\n",
    "        if cv2.waitKey(1)& 0xFF == ord('q'):\n",
    "            break\n",
    "\n",
    "    cap.release()\n",
    "    cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a90ffb20-aa8a-4aeb-b459-48eda04df29d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 363, 308]\n",
      "[4, 360, 305]\n",
      "[4, 360, 298]\n",
      "[4, 363, 299]\n",
      "[4, 372, 291]\n",
      "[4, 372, 292]\n",
      "[4, 375, 290]\n",
      "[4, 377, 290]\n",
      "[4, 377, 287]\n",
      "[4, 378, 288]\n",
      "[4, 378, 286]\n",
      "[4, 378, 285]\n",
      "[4, 377, 285]\n",
      "[4, 385, 258]\n",
      "[4, 388, 252]\n",
      "[4, 395, 248]\n",
      "[4, 407, 245]\n",
      "[4, 417, 240]\n",
      "[4, 434, 242]\n",
      "[4, 444, 246]\n",
      "[4, 450, 247]\n",
      "[4, 462, 258]\n",
      "[4, 460, 261]\n",
      "[4, 461, 263]\n",
      "[4, 460, 265]\n",
      "[4, 458, 267]\n",
      "[4, 458, 269]\n",
      "[4, 457, 269]\n",
      "[4, 450, 280]\n",
      "[4, 451, 285]\n",
      "[4, 450, 283]\n",
      "[4, 444, 283]\n",
      "[4, 437, 282]\n",
      "[4, 437, 283]\n",
      "[4, 433, 283]\n",
      "[4, 425, 283]\n",
      "[4, 379, 281]\n",
      "[4, 367, 288]\n",
      "[4, 354, 288]\n",
      "[4, 358, 288]\n",
      "[4, 344, 293]\n",
      "[4, 338, 296]\n",
      "[4, 328, 304]\n",
      "[4, 325, 310]\n",
      "[4, 325, 312]\n",
      "[4, 320, 315]\n",
      "[4, 322, 314]\n",
      "[4, 317, 317]\n",
      "[4, 311, 318]\n",
      "[4, 308, 321]\n",
      "[4, 310, 322]\n",
      "[4, 312, 323]\n",
      "[4, 312, 322]\n",
      "[4, 315, 319]\n",
      "[4, 319, 316]\n",
      "[4, 324, 314]\n",
      "[4, 327, 310]\n",
      "[4, 368, 279]\n",
      "[4, 364, 272]\n",
      "[4, 364, 272]\n",
      "[4, 360, 273]\n",
      "[4, 357, 273]\n",
      "[4, 355, 276]\n",
      "[4, 354, 277]\n",
      "[4, 354, 279]\n",
      "[4, 353, 281]\n",
      "[4, 352, 280]\n",
      "[4, 353, 281]\n",
      "[4, 352, 280]\n",
      "[4, 353, 277]\n",
      "[4, 352, 278]\n",
      "[4, 356, 278]\n",
      "[4, 354, 277]\n",
      "[4, 357, 278]\n",
      "[4, 357, 276]\n",
      "[4, 356, 277]\n",
      "[4, 363, 274]\n",
      "[4, 364, 278]\n",
      "[4, 366, 282]\n",
      "[4, 373, 290]\n",
      "[4, 422, 353]\n"
     ]
    }
   ],
   "source": [
    "if __name__==\"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fa7f21d0-854f-4a4e-bcfc-ef028898612f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
