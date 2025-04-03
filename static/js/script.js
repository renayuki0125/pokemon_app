let chartInstance = null;

        // 検索ランキングボタンをクリックしたときの処理
        document.getElementById('showRankingBtn').addEventListener('click', function () {
            // サーバーにGETリクエストを送信して最新のランキングデータを取得
            fetch(`/ranking?timestamp=${new Date().getTime()}`) // キャッシュ回避用クエリを追加
                .then(response => response.json()) // レスポンスをJSON形式に変換
                .then(data => { // データを受け取ったら処理を実行
                    // データからポケモン名と検索回数を抽出
                    const labels = data.map(item => item.name);
                    const counts = data.map(item => item.count);

                    // グラフ描画のためのCanvasコンテキストを取得
                    const ctx = document.getElementById('rankingChart').getContext('2d');

                    // 既存のグラフがあれば破棄
                    if (chartInstance) {
                        chartInstance.destroy();
                    }

                    // 新しいグラフを描画
                    chartInstance = new Chart(ctx, {
                        type: 'bar', // 棒グラフを指定
                        data: {
                            labels: labels, // X軸のラベル（ポケモン名）
                            datasets: [{
                                label: '検索回数', // データセットのラベル
                                data: counts, // Y軸のデータ（検索回数）
                                backgroundColor: 'rgba(75, 192, 192, 0.2)', // 棒の背景色
                                borderColor: 'rgba(75, 192, 192, 1)', // 棒の枠線の色
                                borderWidth: 1 // 枠線の幅
                            }]
                        },
                        options: {
                            responsive: true, // 画面サイズに応じて調整
                            scales: {
                                y: { // Y軸の設定
                                    beginAtZero: true // Y軸を0から開始
                                }
                            }
                        }
                    });
                })
                .catch(error => console.error('ランキングデータ取得中にエラーが発生しました:', error)); // エラーハンドリング
        });
