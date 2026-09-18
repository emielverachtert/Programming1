def coins(amount):
    vijfeuromunten = amount // 5
    amount = amount - (vijfeuromunten * 5)

    twee_euromunten = amount // 2
    amount = amount - (twee_euromunten * 2)

    een_euromunten = amount // 1
    amount = amount -(een_euromunten * 1)

    return vijfeuromunten  + twee_euromunten +  een_euromunten

