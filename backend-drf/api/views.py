from datetime import datetime
import os
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StockPredictionSerializer
from rest_framework.response import Response
from rest_framework import status
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class StockPredictionAPIView(APIView):
    def post(self, request):
        serializer = StockPredictionSerializer(data = request.data)
        if serializer.is_valid():
            ticker = serializer.validated_data['ticker']
            # Fetch the data from yfinance
            now = datetime.now()
            start = datetime(now.year-10, now.month,now.day)
            end = now
            df = yf.download(ticker, start, end)
            if df.empty:
                return Response({"error":"No data found for the given ticker", "status":status.HTTP_404_NOT_FOUND})
            df = df.reset_index()
            # Generate Basic Plot
            plt.switch_backend('AGG')
            plt.figure(figsize=(12,5))
            plt.plot(df.Close, label = 'Closing Price')
            plt.title(f"Closing price of {ticker}")
            plt.xlabel('Days')
            plt.ylabel('Close price')
            plt.legend()
            # Save the plot to a file
            plot_img_path = f"{ticker}_plot.png"
            image_path = os
            
            
            return Response({'status': 'success','ticker' : ticker})