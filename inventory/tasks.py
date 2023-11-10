from __future__ import absolute_import

import datetime

from celery import shared_task
from dateutil.relativedelta import relativedelta

from plantation.models import Batch


@shared_task
def task_prune_batch():
    batchs_prune = {}
    batchs = Batch.objects.all()

    for batch in batchs:
        if batch.pruning_date:
            prune_date = batch.pruning_date + relativedelta(years=2)
        else:
            prune_date = batch.planting_date + relativedelta(years=2)

        pruning_days = prune_date - datetime.date.today()
        if pruning_days.days <= 10:
            batchs_prune[batch.code] = batch

    if batchs_prune:
        # TODO: Implementar que se genere una notificación
        return f"Advertencia de lotes que necesitan podar: {batchs_prune}"
