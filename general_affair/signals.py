from django_fsm.signals import post_transition as fsm_post_transition

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.db.models import Sum

from general_affair.models import PurchaseOrder, OrderReceipt, ItemIssued


def calculate_item_stock(item):
    """Calculate item stock.

    Calculating availability of item stock by substracting total quanity
    of issed item and by total quantity of order received for the item.

    Return
    ------
    int

    """
    quantity = 0
    order_receipt = OrderReceipt.objects.filter(purchase_order__item=item)
    if order_receipt.count() >= 1:
        quantity += order_receipt.aggregate(total=Sum('quantity'))['total']
    item_issued = ItemIssued.objects.filter(item=item)
    if item_issued.count() >= 1:
        quantity -= item_issued.aggregate(total=Sum('quantity'))['total']
    return quantity


@receiver(fsm_post_transition, sender=PurchaseOrder)
def db_state_transition_update(sender, instance=None, target=None, **kwargs):
    if not isinstance(instance, sender):
        return
    instance.state = target
    instance.save(update_fields=['state'])


@receiver(post_save, sender=OrderReceipt)
def item_stock_update_on_order_receipt(sender, instance, created, **kwargs):
    item = instance.purchase_order.item
    item.stock = calculate_item_stock(item)
    item.save(update_fields=['stock'])


@receiver(post_delete, sender=OrderReceipt)
def item_stock_update_on_order_receipt_delete(sender, instance, **kwargs):
    item = instance.purchase_order.item
    item.stock = calculate_item_stock(item)
    item.save(update_fields=['stock'])


@receiver(post_save, sender=ItemIssued)
def item_stock_update_on_item_issued(sender, instance, created, **kwargs):
    item = instance.item
    item.stock = calculate_item_stock(item)
    item.save(update_fields=['stock'])


@receiver(post_delete, sender=ItemIssued)
def item_stock_update_on_cancel_item_issued(sender, instance, **kwargs):
    item = instance.item
    item.stock = calculate_item_stock(item)
    item.save(update_fields=['stock'])
