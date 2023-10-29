from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import timedelta, datetime

from post.models import Post


class analyticsAPIView(APIView):
    def get(self, request):
        hashtag = request.query_params.get("hashtag")
        value_type = request.query_params.get("value", "count")
        calculation_type = request.query_params.get("type", "date")

        if calculation_type not in ["date", "hour"]:
            return Response("type 파라메터를 date, hour로 작성해주세요.", status=400)
        now = datetime.now()

        if "start" in request.query_params:
            start_str = request.query_params["start"]
            if calculation_type == "date":
                start_date = datetime.strptime(start_str, "%Y-%m-%d").date()
            elif calculation_type == "hour":
                start_date = datetime.strptime(start_str, "%Y-%m-%d %H:%M")
        else:
            if calculation_type == "date":
                start_date = (now - timedelta(days=7)).date()
            elif calculation_type == "hour":
                start_date = now - timedelta(days=7)

        if "end" in request.query_params:
            end_str = request.query_params["end"]
            if calculation_type == "date":
                end_date = datetime.strptime(end_str, "%Y-%m-%d").date()
            elif calculation_type == "hour":
                end_date = datetime.strptime(end_str, "%Y-%m-%d %H:%M")
        else:
            if calculation_type == "date":
                end_date = now.date()
            elif calculation_type == "hour":
                end_date = now

        if calculation_type == "date" and (end_date - start_date).days > 30:
            return Response({"최대 한달(30일) 조회 가능합니다."}, status=400)
        elif calculation_type == "hour" and (end_date - start_date).days > 7:
            return Response({"최대 일주일(7일) 조회 가능합니다."}, status=400)

        if hashtag is None:
            qs = Post.objects.filter(
                created_at__range=[start_date, end_date + timedelta(days=1)],
            )
        else:
            qs = Post.objects.filter(
                hashtags__name__iexact=hashtag,
                created_at__range=[start_date, end_date + timedelta(days=1)],
            )
        breakpoint()
