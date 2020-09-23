* payment_transactions:
    - progress (USER_REQUESTED, PAYMENT_SENT, PAYMENT_RECEIVED, ..., BILLING_UPDATED)
    - status (PENDING, FAILED, CANCEL, SUCCESS...)
    - package_id
    - package_name
    - package_price
    - package_duration
    - user_id
    - user_name
    - payment_method
    - payment_logs_id
    _ billing_id
    - timestamps
    - lastest (this one is optional, can help to avoid sorting over timestamps)
    ...

* billing:
    - user
    - package
    - transaction_id
    - started_date
    - expired_date
    - timestamps
    ...

* appstore_payment_history:
(* playstore_payment_history:)
    - url
    - post_request
    - response_request
    - transaction_id
    - timestamps
    ...

