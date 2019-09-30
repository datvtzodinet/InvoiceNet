# InvoiceNet
A deep neural network to extract information from invoice documents.

## Instructions
Before training, you need to create a vocabulary and embeddings that the model uses for learning.
```
python3 embeddings.py --data_dir [directory containing training data]
```

#### Training:
To start training InvoiceNet:

```
python3 train.py --data_dir [directory containing training data]
```
> To get more information about how to run the train.py script:
> ```
> python3 train.py -h
> ```

#### Extraction:

To extract information from invoice using the trained model:

```
python3 predict.py --data_dir [directory containing invoices] --model_path [path to trained model]
```
> To get more information about how to run the predict.py script:
> ```
> python3 predict.py -h
> ```