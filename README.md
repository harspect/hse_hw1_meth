# hse_hw1_meth

[Ссылка на Colab notebook](https://colab.research.google.com/drive/1eflogSbJVe9mPT4JNg01PI6u-MTN1NQs)

## Отчет _SRR3824222_1.fastq_

| Параметр                     | SRR3824222_1.fastq                           |
|:----------------------------:|:--------------------------------------------:|
| Basic statistics             | ![22_basic_stat](img/73_1.png) |
| Per base sequence content    | ![22_per_base](img/73_2.png)     |
| Per sequence GC content      | ![22_per_seq](img/73_3.png)       |

### Особенности в сравнении с секвенированием ДНК или РНК:
В _Per base sequence content_ видно, что уровень цитозинов довольно низкий, почти нулевой; cодержание гуанина, также низкое.

В _Per sequence GC content_ заметно следующее: нормальное распределение смещено влево. Это отражает данные из _Basic statistics_.

## Риды

|  Sequence  | _11347700-11367700_ | _40185800-40195800_ | Deduplication |
|:----------:|:-------------------:|:-------------------:|:-------------:|
| Epiblast | 2328                | 1062                | 97.08%        |
| ICM | 1456                | 630                 | 90.92%        |
| 8 Cell | 1090                | 464                 | 81.69%        |

### bash-скрипт для выполнения дедупликации для всех образцов одновременно:
```
! ls *pe.bam | xargs -P 4 -tI{} deduplicate_bismark  --bam  --paired  -o s_{} {}
```

## M-Bias

| Последовательность | 1 рид                                                  | 2 рид                                                  |
|:------------------:|:------------------------------------------------------:|:------------------------------------------------------:|
| SRR3824222         | ![Bis_M-b_1_22](img/22-1.png)      | ![Bis_M-b_2_22](img/22-2.png)      |
| SRR5836473         | ![Bis_M-b_1_73](img/73-1.png)      | ![Bis_M-b_2_73](img/73-2.png)      |
| SRR5836475         | ![Bis_M-b_1_75](img/75-1.png)      | ![Bis_M-b_2_75](img/75-2.png)      |

## Распределение метелирования цитозинов по хромосоме

### Код для отрисовки plot на python ():
```
import pandas as pd
from matplotlib import pyplot as plt

def create_plot(id):
  path = f'/content/s_{id}_1_bismark_bt2_pe.deduplicated.bedGraph'
  bg = pd.read_csv(path,  delimiter='\t', skiprows=1, header=None)
  with plt.style.context('seaborn'):  
    fig = plt.figure(figsize=(15, 5))
    plt.title(id) 
    plt.hist(bg[3], bins=100, density=True)
    plt.xlabel('Percentage')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

l = ['SRR3824222', 'SRR5836473', 'SRR5836475'];
for one in l:
  create_plot(one)
```

| **Название** | **Гистограмма**             |
|:------------:|:---------------------------:|
| Epiblast     | ![hist_22](img/22.png) |
| 8 cell        | ![hist_73](img/73.png) |
| ICM          | ![hist_75](img/75.png) |

## Уровень метелирования и покрытия

для _3100030-3400030_

![cov](img/image_cov_1.png)
