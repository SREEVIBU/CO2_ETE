def run_models(models, x_train_scaled, y_train, x_test_scaled, y_test):
    import mlflow
    import mlflow.sklearn
    from sklearn.metrics import r2_score, mean_squared_error
    import numpy as np

    for name, model in models.items():
        with mlflow.start_run(run_name=name) as run:
            print(f"\n{name} Results:")
            model.fit(x_train_scaled, y_train)
            y_pred = model.predict(x_test_scaled)
            r2 = r2_score(y_test, y_pred)
            n = x_test_scaled.shape[0]
            p = x_test_scaled.shape[1]
            adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
            mse = mean_squared_error(y_test, y_pred)
            rmse = np.sqrt(mse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("adjusted_r2", adj_r2)
            mlflow.log_metric("mse", mse)
            mlflow.log_metric("rmse", rmse)
            # mlflow.sklearn.log_model(model, artifact_path="model", input_example=x_train_scaled[:5])

            print(f"Run completed. Run ID: {run.info.run_id}")